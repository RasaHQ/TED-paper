#!/usr/bin/env bash
set -e
echo

loc_compute="$(pwd)/compute"

# Helper functions
#################################################

notify () {
    MSG=$1
    echo ${MSG}
}

raise () {
    MSG="ERROR: ${1}"
    notify "${MSG}"
    exit 1
}

ask() {
    # Original: https://gist.github.com/davejamesmiller/1965569
    local prompt default reply

    if [[ "${2:-}" = "Y" ]]; then
        prompt="Y/n"
        default=Y
    elif [[ "${2:-}" = "N" ]]; then
        prompt="y/N"
        default=N
    else
        prompt="y/n"
        default=
    fi

    while true; do

        # Ask the question (not using "read -p" as it uses stderr not stdout)
        echo -n "$1 [$prompt] "

        read reply

        # Default?
        if [[ -z "$reply" ]]; then
            reply=${default}
        fi

        # Check if the reply is valid
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac

    done
}

# Gather information
#################################################

if [[ -z "$STY" ]]; then
    if ! ask "WARNING: You are not in a screen environment. Continue?" "N"; then
        exit 1
    fi
    echo
fi

echo "Rasa installation directory:"
readarray -t rasainfo < <( pip show rasa )
rasadir=${rasainfo[7]:10}
echo ${rasadir}
echo

echo "Current Rasa commit:"
rasacommit="$(git --git-dir="${rasadir}/.git" log --pretty=format:'%H' -n 1)"
echo ${rasacommit}
echo

echo "Current Rasa branch:"
rasabranch="$(git --git-dir="${rasadir}/.git" branch | grep \* | cut -d ' ' -f2)"
echo ${rasabranch}
echo

echo "Which experiment(s) would you like to run?"
python3 ask_computation.py  # Without parameters, the list of experiments is printed

echo
echo -n "I want to run experiment(s) number [space separated list]: "
read experiment
readarray -t experiments < <( python3 ask_computation.py ${experiment} )

# Confirmation
#################################################

echo "You chose "
for e in "${experiments[@]}"; do
    echo "> ${e}"
    if [[ ! -f "${loc_compute/}/${e}/train.sh" ]]; then
        echo "Cannot find training script for ${e}."
        exit 1
    fi

    if [[ ! -f "${loc_compute/}/${e}/test-train.sh" ]]; then
        echo "Cannot find testing (train) script for ${e}."
        exit 1
    fi

    if [[ ! -f "${loc_compute/}/${e}/test-test.sh" ]]; then
        echo "Cannot find testing (test) script for ${e}."
        exit 1
    fi
done

num_experiments=${#experiments[@]}

echo
if ! ask "Ready to start ${num_experiments} experiment(s). Continue?" "N"; then
    exit 1
fi

# Run experiments
#################################################

echo
n=1
for e in "${experiments[@]}"; do

    README="${loc_compute}/${e}/README.md"
    echo "" >> ${README}
    echo "## Execution info" >> ${README}
    echo "" >> ${README}
    echo "Rasa branch:" >> ${README}
    echo "${rasacommit} (${rasabranch})" >> ${README}
    echo "" >> ${README}
    echo "Start of experiment: " >> ${README}
    DATE=`date '+%Y%m%d-%H%M%S'`
    echo "${DATE}" >> ${README}
    echo "" >> ${README}

    notify "Experiment ${n}/${num_experiments}, ${e}: START OF EXPERIMENT"

    notify "Experiment ${n}/${num_experiments}, ${e}: Training..."
    ${loc_compute/}/${e}/train.sh || raise "Experiment ${e} failed!"

    echo "End of training / start of testing: " >> ${README}
    DATE=`date '+%Y%m%d-%H%M%S'`
    echo "${DATE}" >> ${README}
    echo "" >> ${README}

    notify "Experiment ${n}/${num_experiments}, ${e}: Testing (train)..."
    ${loc_compute/}/${e}/test-train.sh || raise "Experiment ${e} failed!"

    notify "Experiment ${n}/${num_experiments}, ${e}: Testing (test)..."
    ${loc_compute/}/${e}/test-test.sh || raise "Experiment ${e} failed!"

    notify "Experiment ${n}/${num_experiments}, ${e}: Packing files..."

    cd ${loc_compute/}
    zip -r -q ${e%/}.zip ${e} || raise "Experiment ${e} failed!"
    cd -

    echo "End of experiment: " >> ${README}
    DATE=`date '+%Y%m%d-%H%M%S'`
    echo "${DATE}" >> ${README}
    echo "" >> ${README}

    notify "Experiment ${n}/${num_experiments}, ${e}: END OF EXPERIMENT"

    let "n++"
done

echo "Done."

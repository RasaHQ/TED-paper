#!/usr/bin/env bash
set -e
echo

loc_multiwoz="$(pwd)"
loc_package="$(pwd)/multiwoz"
loc_compute="$(pwd)/compute"
loc_scripts="${loc_package}/scripts"
loc_data="${loc_package}/data"

# Helper functions
#################################################

generate_modular() {
  # Parse stories
  # Creates: stories_all.md, stories_testlist.md, stories_vallist.md, domain.yml
  PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/parse_stories.py "${PARAMS[@]}"

  # Copy files
  echo
  mkdir ${loc_compute}/${config_name}
  echo "Copying template files..."
  cp -r ${loc_compute}/template/. ${loc_compute}/${config_name}
  echo "Copying domain file..."
  cp "${loc_data}/domain.yml" "${loc_compute}/${config_name}/domain.yml"

  echo "*" > "${loc_compute}/${config_name}/.gitignore"

  # Split training/testing set
  python3 "${loc_scripts}/prepare_stories.py" \
      "${loc_data}/stories_all.md" \
      --train "${loc_compute}/${config_name}/data/train/stories.md" \
      --test "${loc_compute}/${config_name}/data/test/stories.md" \
      --num-train ${config_num_train}

  # Write README
  README="${loc_compute}/${config_name}/README.md"
  echo "Writing README.md..."
  echo "## ${config_title}                             " >> ${README}
  echo "                                               " >> ${README}
  echo "date:         ${DATE}                          " >> ${README}
  echo "framework:    modular                          " >> ${README}
  echo "max_history:  ${MAX_HISTORY}                   " >> ${README}
  echo "status slots: ${config_add_status_slots}       " >> ${README}
  echo "                                               " >> ${README}

  # Write Configuration file
  CONFIG="${loc_compute}/${config_name}/config.yml"
  echo "Writing config.yml..."
  echo "# Configuration for Rasa NLU.                                 " >> ${CONFIG}
  echo "# https://rasa.com/docs/rasa/nlu/components/                  " >> ${CONFIG}
  echo "language: en                                                  " >> ${CONFIG}
  echo "pipeline: supervised_embeddings                               " >> ${CONFIG}
  echo "                                                              " >> ${CONFIG}
  echo "# Configuration for Rasa Core.                                " >> ${CONFIG}
  echo "# https://rasa.com/docs/rasa/core/policies/                   " >> ${CONFIG}
  echo "policies:                                                     " >> ${CONFIG}
  echo "  - name: EmbeddingPolicy                                     " >> ${CONFIG}
  echo "    max_history: ${MAX_HISTORY}  # default: 5                 " >> ${CONFIG}
  echo "    batch_strategy: \"sequence\" # default: \"balanced\"      " >> ${CONFIG}
  echo "    epochs: 100 # default: 1                                  " >> ${CONFIG}
  echo "    random_seed: 2019  # default: null                        " >> ${CONFIG}
  echo "    evaluate_on_num_examples: 0 # default: 100                " >> ${CONFIG}
  echo "  - name: FormPolicy                                          " >> ${CONFIG}
}

generate_e2e() {
  # Parse stories
  # Creates: stories_all.md, stories_testlist.md, stories_vallist.md, domain.yml
  PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/parse_stories_e2e.py "${PARAMS[@]}"

  # Copy files
  echo
  mkdir ${loc_compute}/${config_name}
  echo "Copying template files..."
  cp -r ${loc_compute}/template/. ${loc_compute}/${config_name}
  echo "Copying domain file..."
  cp "${loc_data}/domain.yml" "${loc_compute}/${config_name}/domain.yml"
  echo "Copying action map file..."
  cp "${loc_data}/action_map.json" "${loc_compute}/${config_name}-keras/action_map.json"

  echo "*" > "${loc_compute}/${config_name}/.gitignore"

  # Split training/testing set
  python3 "${loc_scripts}/prepare_stories.py" \
      "${loc_data}/stories_all.md" \
      --train "${loc_compute}/${config_name}/data/train/stories.md" \
      --test "${loc_compute}/${config_name}/data/test/stories.md" \
      --num-train ${config_num_train}

  # Write README
  README="${loc_compute}/${config_name}/README.md"
  echo "Writing README.md..."
  echo "## ${config_title}                             " >> ${README}
  echo "                                               " >> ${README}
  echo "date:         ${DATE}                          " >> ${README}
  echo "framework:    end-to-end                       " >> ${README}
  echo "max_history:  ${MAX_HISTORY}                   " >> ${README}
  echo "status slots: ${config_add_status_slots}       " >> ${README}
  echo "                                               " >> ${README}

  # Write Configuration file
  CONFIG="${loc_compute}/${config_name}/config.yml"
  echo "Writing config.yml..."
  echo "# Configuration for Rasa NLU.                                 " >> ${CONFIG}
  echo "# https://rasa.com/docs/rasa/nlu/components/                  " >> ${CONFIG}
  echo "language: en                                                  " >> ${CONFIG}
  echo "pipeline: supervised_embeddings                               " >> ${CONFIG}
  echo "                                                              " >> ${CONFIG}
  echo "# Configuration for Rasa Core.                                " >> ${CONFIG}
  echo "# https://rasa.com/docs/rasa/core/policies/                   " >> ${CONFIG}
  echo "policies:                                                     " >> ${CONFIG}
  echo "  - name: EmbeddingPolicy                                     " >> ${CONFIG}
  echo "    max_history: ${MAX_HISTORY}  # default: 5                 " >> ${CONFIG}
  echo "    batch_strategy: \"sequence\" # default: \"balanced\"      " >> ${CONFIG}
  echo "    epochs: 100 # default: 1                                  " >> ${CONFIG}
  echo "    random_seed: 2019  # default: null                        " >> ${CONFIG}
  echo "    evaluate_on_num_examples: 0 # default: 100                " >> ${CONFIG}
  echo "  - name: FormPolicy                                          " >> ${CONFIG}
}

# Basic configuration
#################################################

params_default=("${loc_data}")
params_default+=(--subset test)
params_default+=(--dataset-version "2.1")
params_default+=(--slot-simplification 3)

config_num_train=740

# Welcome
#################################################

echo "Source code location:"
echo ${loc_package}
echo

echo "Current date and time:"
DATE=$(date '+%Y%m%d-%H%M%S')
echo ${DATE}
echo

# Configuration: max_history=2
#################################################

echo
echo "Configuration: max_history=2 (modular)"
config_title="modular-mh2"
config_name="${DATE}-${config_title}"
MAX_HISTORY=2
config_add_status_slots="n"
# Parameter list for parser
PARAMS=("${params_default[@]}")

generate_modular

echo
echo "Configuration: max_history=2 (end-to-end)"
config_title="e2e-mh2"
config_name="${DATE}-${config_title}"
MAX_HISTORY=2
config_add_status_slots="n"
# Parameter list for parser
PARAMS=("${params_default[@]}")

generate_e2e

# Configuration: max_history=2 with status slots
#################################################

echo
echo "Configuration: max_history=2 with status slots (modular)"
config_title="modular-mh2-status"
config_name="${DATE}-${config_title}"
MAX_HISTORY=2
config_add_status_slots="y"
# Parameter list for parser
PARAMS=("${params_default[@]}")
PARAMS+=(--add-status-slots)

generate_modular

echo
echo "Configuration: max_history=2 with status slots (end-to-end)"
config_title="e2e-mh2-status"
config_name="${DATE}-${config_title}"
MAX_HISTORY=2
config_add_status_slots="y"
# Parameter list for parser
PARAMS=("${params_default[@]}")
PARAMS+=(--add-status-slots)

generate_e2e

# Configuration: max_history=10
#################################################

echo
echo "Configuration: max_history=10 (modular)"
config_title="modular-mh10"
config_name="${DATE}-${config_title}"
MAX_HISTORY=10
config_add_status_slots="n"
# Parameter list for parser
PARAMS=("${params_default[@]}")

generate_modular

echo
echo "Configuration: max_history=10 (end-to-end)"
config_title="e2e-mh10"
config_name="${DATE}-${config_title}"
MAX_HISTORY=10
config_add_status_slots="n"
# Parameter list for parser
PARAMS=("${params_default[@]}")

generate_e2e

# Configuration: max_history=10 with status slots
#################################################

echo
echo "Configuration: max_history=10 with status slots (modular)"
config_title="modular-mh10-status"
config_name="${DATE}-${config_title}"
MAX_HISTORY=10
config_add_status_slots="y"
# Parameter list for parser
PARAMS=("${params_default[@]}")
PARAMS+=(--add-status-slots)

generate_modular

echo
echo "Configuration: max_history=10 with status slots (end-to-end)"
config_title="e2e-mh10-status"
config_name="${DATE}-${config_title}"
MAX_HISTORY=10
config_add_status_slots="y"
# Parameter list for parser
PARAMS=("${params_default[@]}")
PARAMS+=(--add-status-slots)

generate_e2e


echo "Done."

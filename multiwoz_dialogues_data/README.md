# MultiWOZ experiments

- Experimental results under https://github.com/RasaHQ/TED-paper/tree/master/multiwoz_dialogues_data/compute
- To download and parse MultiWOZ 2.1 stories, run `setup.py`
- To run experiments after setup, run `run.py` and select which experiments to run
- Each experiment is in its own directory
- Remember to switch to correct branches of Rasa installation when running end-to-end or modular experiments
  - For end-to-end MultiWOZ experiments, we used rasa branch [e2e_core](https://github.com/RasaHQ/rasa/tree/e2e_core) (commit [2951bd8](https://github.com/RasaHQ/rasa/commit/2951bd8acfb9f2915ac97f78e4e585944837a461))
  - For modular MultiuWOZ experiments we used rasa branch [pub_2019_CoreTransformer_modular](https://github.com/RasaHQ/rasa/tree/pub_2019_CoreTransformer_modular) (commit [2d0914a](https://github.com/RasaHQ/rasa/commit/2d0914a5110d6a179e6a045dcf9c01e45bd9fb54))

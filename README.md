# AI_MAX78000
Machine Learning using the MAX78000

Environment to start development using the ANN accelerator of the MAX78000

# Initial Setup
After you cloned this repository, use `init_environment.sh` to initialise all submodules and setup the required python virtual environments.  For the compilation special compilers are needed. The script `get_compilers.sh` downloads them into the project folder and extracts the archives. To include the executables into the global `$PATH` the script `setup.sh` helps. This should be executed each time you start a new shell.

# Notes
## TensorFlow
the MAX78000 can work with Tensorflow, which I'm going to use here. There is an issue with the latest versions of the precompiled Tensorflow. They are not compatible with old computers. In case you face a `Invalid Instruction` error, your computer is too old and you'll have to solve this. Downgrading TensorFlow does not work, because Maxim has used some of the later features.

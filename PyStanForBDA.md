# PyStan installation

[Stan](http://mc-stan.org/) (which takes its name in part from Stanislaw Ulam, a co-creator of the earliest Monte Carlo methods) is both a **probabilistic programming language** capable of concisely describing Bayesian graphical models, and a powerful **source-to-source compiler** (with accompanying C++ libraries) that can write C++ code implementing such models, including sophisticated optimization and posterior sampling capability.

Since Stan produces C++ code, it requires users to have mutually compatible compilers and interpreters, a potentially nontrivial software requirement that can make it challenging to install Stan from scratch. Fortunately for Anaconda users, Anaconda developers have worked to simplify the process by automatically providing platform-specific compilers to Anaconda users who install Stan (though this is successful only for specific combinations of Python and Stan interface versions).

The current version of Stan is 2.29.2.

The Stan team provides interfaces to Stan from the command line, and for a variety of computer languages widely used for statistical computing. Note that the interfaces have their own version numbers, distinct from Stan's (e.g., PyStan 2 and PyStan 3 both interface to Stan 2.x). There are two interfaces to Python:

* **CmdStanPy:** This interface provides Python functions that run command-line Stan programs, communicating data between those programs and Python via files.
* **PyStan:** This interface provides Python access to a Stan-compiled C++ library.
  * *PyStan 2* directly accesses the library, communicating data via C++ data structures. It supports Linux, macOS, and Windows users. It is no longer maintained.
  * *PyStan 3* accesses the library via an intermediate HTTP REST API (which potentially can support frontends other than Python). It currently implements only a subset of Stan's capabilities. Windows support has been abandoned for PyStan 3, but Windows users can use it by installing Microsoft's Windows Subsystem for Linux v2 (WSL 2) and installing and using PyStan 3 within the subsystem. PyStan 3 requires some modifications of the Jupyter environment to interact well with Jupyter notebooks.

We will use PyStan 2.19.1.1, the last version of PyStan 2; see the [PyStan 2.19.1.1 documentation](https://pystan2.readthedocs.io/en/latest/).

**Schedule your PyStan installation and testing appropriately.**  Some steps of this setup require downloads that can be time-consuming, depending on network conditions. And there may be installation problems with some platforms. The earlier you can discover problems, the more likely it is that we can find a fix in time for assignments that use Stan.

### Installing PyStan in a new Conda environment

The following straightforward procedure has been tested on macOS 10.15 (Catalina), macOS 11 (Big Sur), and Windows 10 (running in a VMware Fusion virtual machine). For macOS, our tests have used Macs with Intel CPUs, but several students have verified that the instructions below work on the new M1-based Macs. Besides PyStan, this procedure installs Anaconda-produced compilers (a different set for each platform, e.g., `clang` for macOS and `gcc` for Windows 10), along with custom compiler toolchain settings tailored to PyStan's needs.

**Important note:** To support PyStan, conda replaces system-provided compilation tools in your shell's search path, and changes default compiler settings. If you are not currently using a Conda environment for your course work, I strongly recommend that you set up a custom Conda environment for your PyStan work, as described here. By installing PyStan in its own environment, you ensure that your system's default compilation tools and settings remain available in your shell when you have not activated the PyStan environment.

**Note to macOS users:** My Macs all have Apple's Xcode and command-line tools installed. I believe that they are *not* necessary for PyStan to work (since it uses Anaconda-supplied compilers). However, if you have trouble with the PyStan installation or test, consider installing Apple's developer tools, as described at the end of this document. But contact us first with details of your problem; there may be a simpler fix.

**PyStan installation (all platforms):** Perform the following steps in order:

1. Update the `conda` command-line package manager in a terminal/shell session by running the following command ("$" denotes the terminal prompt; this may take a several minutes if you haven't updated `conda` since the start of the semester):

```bash
$ conda update conda
```
2. Create a new **`py37stan2`** environment containing Python 3.7 (*not* the current version, Python 3.9) and PyStan 2.19.1.1 with the following command (entered as a single line of text). This command adds some potentially useful additional packages to the environment, in particular, the [ArviZ](https://arviz-devs.github.io/arviz/index.html) package for plotting and analysis of  posterior sampler output. This environment contains many fewer packages than the `bda22` environment used earlier in the course, and should install more quickly. (This takes about 4 minutes on my Mac, with my home internet connection.)

```bash
$ conda create -n py37stan2  -c conda-forge python=3.7 numpy scipy pandas matplotlib seaborn notebook pystan=2.19.1.1 arviz 
```
3. **For Windows users only:** By default, when Python on Windows is told to compile C++ to build an external program or library, it looks for a compiler that is not provided with Windows. The `conda-forge` version of PyStan requires that Python instead invoke a Linux-based free compiler, which gets installed by the `conda create` command. Windows users need to modify a Python configuration file so that Python uses the `conda`-installed compiler toolchain. Follow the instructions below to do this, before moving to the test step.
4. Test PyStan, as described below. (It runs in about a minute on my Macs, and in a few minutes on Windows 10 running in virtual machine.)



## Windows configuration modification

**For Windows users only:** To complete Step 3 above, do the following in a terminal (e.g., Anaconda prompt):

First, activate the new environment:  

```bash
conda activate py37stan2
```

Next, find the location of the configuration file that controls Python's choice of C++ compiler. Launch Python with the `python` command. Then execute the following two lines of Python (shown here with the `>>>` Python prompt):  

```python
>>> import distutils
>>> print(distutils.__file__)
```

Then quit the Python compiler (e.g., with `Ctrl-Z`, `Enter`), but keep the terminal window open.

That Python `print`  command will print the path for Python's `distutils` package, which PyStan uses to direct compilation of Stan-produced C++ code. The path will look something like this (this is one long line of text; it probably won't look exactly like this for you):

```
C:\Anaconda\envs\py37stan2\lib\site-packages\setuptools\_distutils\__init__.py
```

Select and copy the path up to and including "`distutils`" (your path may not have an underscore before `distutils`); in my case, I copied this part:

```
C:\Anaconda\envs\py37stan2\lib\site-packages\setuptools\_distutils
```

Change your working directory to that directory by typing `cd`, a space, and then pasting that path (then type return):

```bash
cd "C:\Anaconda\envs\py37stan2\lib\site-packages\setuptools\_distutils\__init__.py"
```

Open the Windows File Explorer in that directory by launching it from the command line (note the "`.`" at the end, which denotes the current directory):

```
explorer.exe .
```

In File Explorer, locate the file named `distutils.cfg` (Explorer may hide the `.cfg` part). Open it using a text editor; Notepad or Visual Studio Code will work. Replace the contents of the file with these three lines (the last line is blank; it may not be needed):

```
[build]
compiler=mingw32

```

Save the file. This completes the modification; at this point your PyStan installation should work.



## Test PyStan

First, activate the new Conda environment:

```bash
$ conda activate py37stan2
```

Test PyStan using a Python interpreter by running the following Python code. You can copy and paste it at a Python or IPython interpreter prompt, or download and run the accompanying [PyStanTest.py](PyStanTest.py) script, e.g., with `python PyStanTest.py`, or with  `ipython -i PyStanTest.py`, which uses `ipython` and leaves Python running after the test, in case you'd like to explore the results.

```python
import pystan

# Stan code for a trivial model---a normal prior for
# theta, with no data or likelihood function.
model_code = '''
    parameters {real theta;}
    model {theta ~ normal(0,1);}
'''

# The following will invoke Stan to build and compile a C++
# library; it will take some time and report progress to
# the console.
model = pystan.StanModel(model_code=model_code)

# This will run an MCMC algorithm for 2000 steps, discarding
# the first half of the run as burn-in; it will report progress
# to the console.
results = model.sampling(n_jobs=1)

# Here we print a Monte Carlo estimate of the posterior mean
# for y; if all goes well it should be near 0.
thetas = results.extract()['theta']
print('Mean of posterior samples:  %.4f' % thetas.mean())
```

The output should look something like the text below (note that the compilation step will take up to a couple minutes; PyStan is composing and compiling quite a bit of code, even for this simple example). You may see lines reporting compiler *warnings* (perhaps many, many such lines). Such warnings are innocuous and may be ignored. Compiler *errors* are signs of trouble; they will typically halt the code via a Python exception.
```
INFO:pystan:COMPILING THE C++ CODE FOR MODEL anon_model_6fa7f15b3d85e088d23232eb587e3d58 NOW.

Gradient evaluation took 5e-06 seconds
1000 transitions using 10 leapfrog steps per transition would take 0.05 seconds.
Adjust your expectations accordingly!


Iteration:    1 / 2000 [  0%]  (Warmup)
Iteration:  200 / 2000 [ 10%]  (Warmup)
Iteration:  400 / 2000 [ 20%]  (Warmup)
Iteration:  600 / 2000 [ 30%]  (Warmup)
Iteration:  800 / 2000 [ 40%]  (Warmup)
Iteration: 1000 / 2000 [ 50%]  (Warmup)
Iteration: 1001 / 2000 [ 50%]  (Sampling)
Iteration: 1200 / 2000 [ 60%]  (Sampling)
Iteration: 1400 / 2000 [ 70%]  (Sampling)
Iteration: 1600 / 2000 [ 80%]  (Sampling)
Iteration: 1800 / 2000 [ 90%]  (Sampling)
Iteration: 2000 / 2000 [100%]  (Sampling)

 Elapsed Time: 0.009932 seconds (Warm-up)
               0.008974 seconds (Sampling)
               0.018906 seconds (Total)

[There will be 4 sections like this, corresponding to 4 separate sample paths being produced.]

Mean of posterior samples:  -0.0162

[You won't get that precise value for the mean, but it should be near 0.]
```

The compilation step is time-consuming, but for this trivial model, running the sampler is very fast. If you'd like to run the sampler again (maybe to double-check that the mean is near zero), use the `ipython` command above (which stays running after the computation finishes), and enter the `results = ...` , `thetas = ...`, and `print...` lines again.

If you encounter problems with the test that you can't resolve yourself, contact us with a description of the problem.



## macOS developer tools

Mac users who do not have Apple's developer tools installed and who have problems with PyStan may consider installing Apple's command-line tools (but if time allows, first consult us with your problem).

The standard way to get Apple's command-line tools is to install *Xcode*, Apple's developer enviroment. That said, Xcode is large (the current version is a 12.7 GB download), and if you don't plan on developing macOS or iOS apps, you may want to install the much smaller command-line tools package by itself. However, to do that, you must have an Apple developer account (it's free). If you want to install the tools alone, you'll find the installer at [Apple Developer downloads](https://developer.apple.com/download/more/) (login required). Otherwise, install the tools by installing Xcode, as follows:

- Download Xcode using the Mac App Store app.  The current version is Xcode 13.  *Note that Xcode is large and the download can be time consuming (sometimes taking hours)—don't postpone this until the last minute.* When first installing Xcode on a new machine, I often start the download at night and leave it to run overnight.
- *Launch Xcode.*  You must launch it after installing; it installs the command-line tools after its first launch. You may then quit it.


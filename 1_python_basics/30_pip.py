# PIP
    # PIP is a package manager for Python packages, or modules if you like.

# What is a Package?
'''
    A package contains all the files you need for a module.
    Modules are Python code libraries you can include in your project.
'''

# Check if PIP is Installed
    # Navigate your command line to the location of Python's script directory, and type the following:
'''
    pip --version
'''

# Install PIP
    # If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

# Download a Package
    # Downloading a package is very easy.
    # Open the command line interface and tell PIP to download the package you want.
'''
    pip install camelcase
'''

# Using a Package
    # Once the package is installed, it is ready to use.
    # Import the "camelcase" package into your project.
'''
    import camelcase

    c = camelcase.CamelCase()
    txt = "hello world"
    print(c.hump(txt))
'''

# Find Packages
    # Find more packages at https://pypi.org/.

# Remove a Package
    # Use the uninstall command to remove a package.
'''
    pip uninstall camelcase
'''

# List Packages
    # Use the list command to list all the packages installed on your system.
'''
    pip list
'''
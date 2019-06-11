# npm2rpm

Useful scripts to convert npm packages to rpm packages (source tar balls, and spec files)

## Install

```
sudo zypper install nodejs rpmdevtools
git clone git@github.com:openSUSE-zh/npm2rpm.git
cd npm2rpm
sudo install npm2rpm /usr/local/bin
sudo install -m 644 spectemplate-nodejs.spec /etc/rpmdevtools/
```

## How it works

Run

```
npm2rpm gulp-cli
```

will generate two files:

1. npmjs-gulp-cli-2.2.0.tar.gz
2. npmjs-gulp-cli.spec

Fill in information and link executable scripts into bin directory. Then your
package is finished!

## What about nodejs-packaging?

This package uses a different approach. It just bundle all dependencies in source
tarball, instead of creating a lot of RPM packages. It doesn't create dependencies.
So it is much easier to maintain and packages work the same way as npm installation.

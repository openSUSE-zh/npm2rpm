#
# spec file for package [spectemplate]
#
# Copyright (c) __YEAR__ SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define npm_name [npm_name]
Name:           [spectemplate]
Version:        0
Release:        0
Summary:
License:
Group:          Development/Languages/NodeJS
URL:            https://www.npmjs.com/package/%{npm_name}
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  nodejs
BuildRequires:  fdupes
Requires:       nodejs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description


%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/node_modules/%{npm_name}
cp -r * %{buildroot}%{_prefix}/lib/node_modules/%{npm_name}
mkdir -p %{buildroot}%{_bindir}
ln -s %{_prefix}/lib/node_modules/%{npm_name}/index.js %{buildroot}%{_bindir}/%{npm_name}

%fdupes %{buildroot}

%check

%files
%license LICENSE
%doc README.md
%{_bindir}/%{npm_name}
%{_prefix}/lib/node_modules

%changelog

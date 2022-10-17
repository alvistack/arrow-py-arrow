# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-arrow
Epoch: 100
Version: 1.2.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Better dates and times for Python
License: Apache-2.0
URL: https://github.com/arrow-py/arrow/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Arrow is a Python library that offers a sensible and human-friendly
approach to creating, manipulating, formatting and converting dates,
times and timestamps. It implements and updates the datetime type,
plugging gaps in functionality and providing an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-arrow
Summary: Better dates and times for Python
Requires: python3
Requires: python3-python-dateutil >= 2.7.0
Requires: python3-typing-extensions
Provides: python3-arrow = %{epoch}:%{version}-%{release}
Provides: python3dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(arrow) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-arrow
Arrow is a Python library that offers a sensible and human-friendly
approach to creating, manipulating, formatting and converting dates,
times and timestamps. It implements and updates the datetime type,
plugging gaps in functionality and providing an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%files -n python%{python3_version_nodots}-arrow
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-arrow
Summary: Better dates and times for Python
Requires: python3
Requires: python3-python-dateutil >= 2.7.0
Requires: python3-typing-extensions
Provides: python3-arrow = %{epoch}:%{version}-%{release}
Provides: python3dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(arrow) = %{epoch}:%{version}-%{release}

%description -n python3-arrow
Arrow is a Python library that offers a sensible and human-friendly
approach to creating, manipulating, formatting and converting dates,
times and timestamps. It implements and updates the datetime type,
plugging gaps in functionality and providing an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%files -n python3-arrow
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-arrow
Summary: Better dates and times for Python
Requires: python3
Requires: python36-dateutil >= 2.7.0
Requires: python3-typing-extensions
Provides: python3-arrow = %{epoch}:%{version}-%{release}
Provides: python3dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(arrow) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-arrow
Arrow is a Python library that offers a sensible and human-friendly
approach to creating, manipulating, formatting and converting dates,
times and timestamps. It implements and updates the datetime type,
plugging gaps in functionality and providing an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%files -n python%{python3_version_nodots}-arrow
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?centos_version} == 700)
%package -n python3-arrow
Summary: Better dates and times for Python
Requires: python3
Requires: python3-dateutil >= 2.7.0
Requires: python3-typing-extensions
Provides: python3-arrow = %{epoch}:%{version}-%{release}
Provides: python3dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(arrow) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-arrow = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(arrow) = %{epoch}:%{version}-%{release}

%description -n python3-arrow
Arrow is a Python library that offers a sensible and human-friendly
approach to creating, manipulating, formatting and converting dates,
times and timestamps. It implements and updates the datetime type,
plugging gaps in functionality and providing an intelligent module API
that supports many common creation scenarios. Simply put, it helps you
work with dates and times with fewer imports and a lot less code.

%files -n python3-arrow
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog

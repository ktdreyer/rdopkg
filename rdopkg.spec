Name:             rdopkg
Version:          0.28
Release:          1%{?dist}
Summary:          RDO packaging automation tool

Group:            Development/Languages
License:          ASL 2.0
URL:              https://github.com/redhat-openstack/rdopkg.git
Source0:          https://pypi.python.org/packages/source/r/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    PyYAML

Requires:         rdopkg-bsources >= %{version}
Requires:         python-rdoupdate >= 0.14
Requires:         python-paramiko
Requires:         python-requests
Requires:         python-setuptools
Requires:         PyYAML
Requires:         git-core
Requires:         git-review
Requires:         koji
# optional but recommended
Requires:         python-blessings


%description
rdopkg is a tool for automating RDO packaging tasks including building and
submitting of new RDO packages.


%package bsources
Summary:         Additional RDO build sources for rdoupdate

Requires:        python-rdoupdate >= 0.14
Requires:        python-beautifulsoup4

%description bsources
This package contains additional rdoupdate build sources used for updating RDO.


%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# man pages
install -d -m 755 %{buildroot}%{_mandir}/man{1,7}
install -p -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 doc/man/*.7 %{buildroot}%{_mandir}/man7/

# additional build sources for rdoupdate
mkdir -p %{buildroot}%{python_sitelib}/rdoupdate/bsources
cp bsources/*.py %{buildroot}%{python_sitelib}/rdoupdate/bsources/

%files
%doc README.md
%doc doc/*.txt doc/html
%license LICENSE
%{_bindir}/rdopkg
%{python_sitelib}/rdopkg
%{python_sitelib}/*.egg-info
%{_mandir}/man1
%{_mandir}/man7

%files bsources
%{python_sitelib}/rdoupdate/bsources/*.py*

%changelog
* Wed Jun 03 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.28-1
- Update to 0.28
- reqquery: manage dem requirements like a boss

* Mon May 04 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.27.1-1
- Update to 0.27.1
- update-patches: create commit even with only removed patches

* Mon Apr 27 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.27-1
- Update to 0.27
- reqcheck: new action to check for correct Requires

* Mon Mar 30 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.26-1
- Update to 0.26
- query: new action to query RDO package versions
- update: use SSH for update repo
- reqdiff: fix stupid regexp
- new-version: ignore missing requirements.txt diff

* Wed Feb 18 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.25-1
- Update to 0.25
- update: parsable update summary in gerrit topic
- Provide set_colors function to control color output

* Wed Feb 04 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.24-1
- Update to upstream 0.24
- update-patches: support %autosetup patch apply method
- Require rdoupdate with cbs support

* Thu Jan 22 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.23.1-1
- Update to 0.23.1
- Packaging fixes

* Tue Jan 20 2015 Jakub Ruzicka <jruzicka@redhat.com> 0.23-1
- Update to 0.23
- kojibuild: offer push when needed
- reqdiff: new action & integrated into new-version
- core: fix state file handling and atomic actions

* Tue Dec 09 2014 Jakub Ruzicka <jruzicka@redhat.com> 0.22-1
- Open source rdopkg

Name:           goss
Version:        0.1
Release:        1.el7.kkruzich
Summary:        goss
Group:          Applications/System
License:        Apache License 2.0
URL:            https://github.com/aelsabbahy/goss
Source1:	goss
Source2:	goss.service
Source3:	goss.base.yaml
Source4:	goss.webserver.yaml

%description
This package contains goss. Goss: Quick and Easy server validation.

Goss is a YAML based serverspec alternative tool for validating a server’s configuration. It eases the process of writing 
tests by allowing the user to generate tests from the current system state. Once the test suite is written they can be 
executed, waited-on, or served as a health endpoint.

See https://github.com/aelsabbahy/goss for details.

%prep

%build

%install

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/goss/goss.d

install -m755 %{SOURCE1} %{buildroot}%{_bindir}/goss
install -m644 %{SOURCE2} %{buildroot}%{_unitdir}/goss.service
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/goss/goss.base.yaml
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/goss/goss.d/goss.webserver.yaml

%files
%defattr(-,root,root)
%{_bindir}/goss
%{_unitdir}/goss.service
%{_sysconfdir}/goss/goss.base.yaml
%{_sysconfdir}/goss/goss.d/goss.webserver.yaml

%changelog
* Wed Feb 21 2018 kkruzich <kkruzich@gmail.com> - 0.1-1
- Initial release

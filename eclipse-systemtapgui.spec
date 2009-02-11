%define eclipse_base        %{_libdir}/eclipse

Name:           eclipse-systemtapgui
Version:        1.0
Release:        %mkrel 1
Summary:        Eclipse plugins for SystemTap

Group:          Development/Other
License:        EPL
URL:            http://stapgui.sourceforge.net/
Source0:        http://downloads.sourceforge.net/stapgui/com.ibm.systemtapgui.src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
BuildRequires:  java-rpmbuild
BuildRequires:  eclipse-pde, eclipse-swt
BuildRequires:  jsch, zip
Requires:       eclipse-platform

%description
Eclipse plugins providing IDE integration and visualization tools for SystemTap


%prep
%setup -q com.ibm.systemtapgui.src



%build
%{eclipse_base}/buildscripts/pdebuild -f \
com.ibm.systemtapgui.systemtap.feature -a "-DjavacSource=1.5 -DjavacTarget=1.5"


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_datadir}/eclipse/dropins/systemtapgui
unzip -q -d %{buildroot}%{_datadir}/eclipse/dropins/systemtapgui \
build/rpmBuild/com.ibm.systemtapgui.systemtap.feature.zip

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/eclipse/dropins/systemtapgui
%doc com.ibm.systemtapgui.systemtap.feature/epl-v10.html

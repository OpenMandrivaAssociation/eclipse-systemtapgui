%define eclipse_base        %{_libdir}/eclipse

Name:           eclipse-systemtapgui
Version:        1.1
Release:        4
Summary:        Eclipse plugins for SystemTap

Group:          Development/Java
License:        EPL
URL:            https://stapgui.sourceforge.net/
Source0:        org.eclipse.linuxtools.systemtap.src.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  eclipse-pde, eclipse-swt
BuildRequires:  eclipse-birt >= 2.5 
BuildRequires:  eclipse-emf
BuildRequires:  jsch
Requires:       eclipse-platform
Requires:       eclipse-birt >= 2.5

%description
Eclipse plugins providing IDE integration and visualization tools for SystemTap


%prep
%setup -q org.eclipse.linuxtools.systemtap 

 

%build
%{eclipse_base}/buildscripts/pdebuild -f \
org.eclipse.linuxtools.systemtap-feature -a "-DjavacSource=1.5 -DjavacTarget=1.5" -d "birt emf rhino"


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_datadir}/eclipse/dropins/systemtapgui
unzip -q -d %{buildroot}%{_datadir}/eclipse/dropins/systemtapgui \
build/rpmBuild/org.eclipse.linuxtools.systemtap-feature.zip

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/eclipse/dropins/systemtapgui
%doc org.eclipse.linuxtools.systemtap-feature/epl-v10.html


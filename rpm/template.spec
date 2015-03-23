Name:           ros-indigo-rocon-apps
Version:        0.7.8
Release:        0%{?dist}
Summary:        ROS rocon_apps package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rocon_apps
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gateway-msgs
Requires:       ros-indigo-rocon-app-manager-msgs
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rospy-tutorials
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin

%description
Core rocon apps for use with the appmanager and rocon concert.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 23 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.8-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.7-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.5-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.4-0
- Autogenerated by Bloom


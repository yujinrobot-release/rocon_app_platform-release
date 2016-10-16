Name:           ros-kinetic-rocon-apps
Version:        0.9.1
Release:        0%{?dist}
Summary:        ROS rocon_apps package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rocon_apps
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gateway-msgs
Requires:       ros-kinetic-rocon-app-manager-msgs
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rospy-tutorials
Requires:       ros-kinetic-topic-tools
BuildRequires:  ros-kinetic-catkin

%description
Core rocon apps for use with the appmanager and rocon concert.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Oct 16 2016 Daniel Stonier <d.stonier@gmail.com> - 0.9.1-0
- Autogenerated by Bloom

* Tue Jun 21 2016 Daniel Stonier <d.stonier@gmail.com> - 0.8.0-0
- Autogenerated by Bloom


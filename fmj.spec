Summary:	Free replacement for the JMF (Java Media Framework)
Name:		fmj
Version:	20071014
Release:	%mkrel 0.0.4
License:	LGPLv3
Group:		Development/Java
URL:		http://fmj.sourceforge.net/
Source0:	%{name}.tar.bz2
Source1:	%{name}.png
Requires:	gstreamer0.10-ffmpeg
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-ugly
Requires:	ffmpeg-java
Requires:	java >= 1.5
Requires:	jlayer
Requires:	jorbis
Requires:	jpackage-utils >= 1.5
Requires:	jre >= 1.5
Requires:	jspeex
#Requires:		liquidlnf
Requires:	mp3spi
Requires:	theora-java
Requires:	tritonus-shared
Requires:	vorbisspi
BuildRequires:	ant
BuildRequires:	ffmpeg-java
BuildRequires:	gstreamer0.10-devel
BuildRequires:	java-rpmbuild >= 1.5
BuildRequires:	jlayer
BuildRequires:	jorbis
BuildRequires:	jspeex
BuildRequires:	junit
BuildRequires:	jpackage-utils >= 1.5
BuildRequires:	mp3spi
BuildRequires:	theora-java
BuildRequires:	tritonus-shared
BuildRequires:	update-alternatives
#BuildRequires:	update-desktop-files
BuildRequires:	vorbisspi
BuildRequires:	xml-commons-apis
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
FMJ is an open-source project with the goal of providing a
replacement or alternative to Java Media Framework (JMF).

It aims to produce a single API/Framework which can be used to
capture, playback, process and stream media across multiple
platforms.

%package javadoc
Summary:	Javadoc for fmj
Group:		Development/Java

%description javadoc
Javadoc for fmj.

%package demo
Summary:	Some examples for fmj
Group:		Development/Java
Requires:	java-devel >= 1.5
Requires:	%{name}

%description demo
Some examples (javacode) for fmj.

%prep
%setup -q -n %{name}
# the build.xml needs every time a rediff, so use sed instead of a patch ... :)
%__sed -i -e 's|<src path="src.ffmpeg-java"/>||g' \
	build.xml
%__sed -i -e 's|<fileset dir="src.ffmpeg-java"/>||g' \
	build.xml
%__sed -i -e 's|<src path="src.theora-java"/>||g' \
	build.xml
%__sed -i -e 's|<fileset dir="src.theora-java"/>||g' \
	build.xml

%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/ffmpeg-java.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/jl1.0.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/tritonus_share.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/mp3spi1.9.4.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/jorbis-0.0.15.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/jogg-0.0.7.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/vorbisspi1.0.2.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/jspeex.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/theora-java.jar" />||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/lib" file="lib/jheora-patch.jar" />||g' \
	build.xml

# unneeded windows/mac files
%__sed -i -e 's|<copy todir="${dist}/native/win32-x86" file="nativelib/win32-x86/civil.dll"/>||g' \
	build.xml
%__sed -i -e 's|<copy todir="${dist}/native/win32-x86" file="nativelib/win32-x86/jdshow.dll"/>||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjstudio.bat" file="sh/win32/x86/fmjstudio.bat" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjregistry.bat" file="sh/win32/x86/fmjregistry.bat" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjplay.bat" file="sh/win32/x86/fmjplay.bat" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjtranscode.bat" file="sh/win32/x86/fmjtranscode.bat" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjstudio-macosx-universal.sh" file="sh/macosx/universal/fmjstudio.sh" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjregistry-macosx-universal.sh" file="sh/macosx/universal/fmjregistry.sh" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjplay-macosx-universal.sh" file="sh/macosx/universal/fmjplay.sh" />||g' \
	build.xml
%__sed -i -e 's|<copy tofile="${dist}/fmjtranscode-macosx-universal.sh" file="sh/macosx/universal/fmjtranscode.sh" />||g' \
	build.xml

# adjust classpath for existing  jar-files
%__sed -i -e 's|lib/ffmpeg-java.jar|%{_javadir}/fmj/ffmpeg-java.jar|g' \
	build.xml
%__sed -i -e 's|lib/jl1.0.jar|%{_javadir}/jl.jar|g' \
	build.xml
%__sed -i -e 's|lib/tritonus_share.jar|%{_javadir}/tritonus_share.jar|g' \
	build.xml
%__sed -i -e 's|lib/mp3spi1.9.4.jar|%{_javadir}/mp3spi.jar|g' \
	build.xml
%__sed -i -e 's|lib/jorbis-0.0.15.jar|%{_javadir}/jorbis.jar|g' \
	build.xml
%__sed -i -e 's|lib/jogg-0.0.7.jar|%{_javadir}/jogg.jar|g' \
	build.xml
%__sed -i -e 's|lib/vorbisspi1.0.2.jar|%{_javadir}/vorbisspi.jar|g' \
	build.xml
%__sed -i -e 's|lib/jspeex.jar|%{_javadir}/jspeex.jar|g' \
	build.xml
%__sed -i -e 's|lib/junit.jar|%{_javadir}/junit.jar|g' \
	build.xml
%__sed -i -e 's|lib/theora-java.jar|%{_javadir}/fmj/theora-java.jar|g' \
	build.xml
%__sed -i -e 's|lib/jheora-patch.jar|%{_javadir}/fmj/jheora-patch.jar|g' \
	build.xml
%__sed -i -e 's|build-ds,build-qt|build-ds|g' \
	build.xml

# remove packaged jar-files
for i in ffmpeg-java jl jogg jorbis jspeex jheora-patch junit mp3spi vorbisspi theora-java tritonus_share; do
	%__rm lib/$i*.jar
done

# remove windows and mac stuff
%__rm -r nativelib/win32-x86
%__rm -r sh/win32
%__rm -r sh/macosx

# adjust path for the samples
%__sed -i -e 's|samplemedia|%{_datadir}/%{name}|g' \
	src.fmjstudio/net/sf/fmj/ui/application/PlayerPanel.java

# adjust path for logging.properties
%__sed -i -e 's|logging.properties|%{_javadir}/%{name}/logging.properties|g' \
	src/net/sf/fmj/utility/FmjStartup.java

%build
export LANG=C
export CLASSPATH=$(build-classpath tritonus/tritonus-shared)
%ant -Dbuild.sysclasspath=first dist

%install
pushd build/dist/%{name}
	# jar
	%__install -dm 755 %{buildroot}%{_javadir}/%{name}
	for i in %{name} %{name}-applet %{name}-nojmf; do
		%__install -pm 644 $i.jar \
			%{buildroot}%{_javadir}/%{name}/$i-%{version}.jar
	done
	pushd %{buildroot}%{_javadir}/%{name}
		for jar in *-%{version}*; do
			ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
		done
	popd
	
	# other jars
	%__install -dm 755 %{buildroot}%{_javadir}/%{name}/lib
	%__install -pm 644 lib/*.jar \
		%{buildroot}%{_javadir}/%{name}/lib
	
	# logging.properties
	%__install -pm 644 *.properties \
		%{buildroot}%{_javadir}/%{name}
	
	# native libs
	%__install -dm 755 %{buildroot}%{_libdir}/%{name}
	%ifnarch x86_64
		%__install -pm 644 native/linux-x86/*.so \
			%{buildroot}%{_libdir}/%{name}
	%else
		%__install -pm 644 native/linux-amd64/*.so \
			%{buildroot}%{_libdir}/%{name}
	%endif
	# fmj tries to load libgstreamer-0.10.so, so to avoid devel-package ...
	pushd %{buildroot}%{_libdir}/%{name}
	#ln -s %{_libdir}/libgstreamer-0.10.so.0 libgstreamer-0.10.so
	popd
	
	# sample-data
	%__install -dm 755 %{buildroot}%{_datadir}/%{name}
	%__install -pm 644 samplemedia/* \
		%{buildroot}%{_datadir}/%{name}
popd

pushd build
	# javadoc
	%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
	mkdir -p doc; touch doc/empty
	%__cp -pr doc/* \
		%{buildroot}%{_javadocdir}/%{name}-%{version}
	ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 
popd

# examples/demos
%__cp -R src.examples.* \
	%{buildroot}%{_datadir}/%{name}
%__install -m 644 applet.example/* \
	%{buildroot}%{_datadir}/%{name}

# startscripts for fmj-*
for i in play registry studio transcode; do
	%__cat > %{name}-$i.sh << EOF
#!/bin/sh

VERBOSE=1
. %{_javadir}-utils/java-functions

set_javacmd
check_java_env
set_jvm_dirs
set_options -Djava.library.path="@LIBRARY_PATH@" -Djava.util.logging.config.file="%{_javadir}/%{name}/logging.properties"

CLASSPATH=\`build-classpath %{name} jl jorbis jspeex liquidlnf mp3spi tritonus_share vorbisspi\`
MAIN_CLASS="net.sf.fmj.ui.@MAIN_CLASS@"
export LD_LIBRARY_PATH=@LIBRARY_PATH@:\$LD_LIBRARY_PATH
run "\$1"
EOF
done

%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{name}-*.sh \
	%{buildroot}%{_bindir}

# set main-class
%__sed -i -e 's|@MAIN_CLASS@|FmjPlay|g' \
	%{buildroot}%{_bindir}/%{name}-play.sh
%__sed -i -e 's|@MAIN_CLASS@|FmjRegistry|g' \
	%{buildroot}%{_bindir}/%{name}-registry.sh
%__sed -i -e 's|@MAIN_CLASS@|FmjStudio|g' \
	%{buildroot}%{_bindir}/%{name}-studio.sh
%__sed -i -e 's|@MAIN_CLASS@|FmjTranscode|g' \
	%{buildroot}%{_bindir}/%{name}-transcode.sh

# set library-paths
for i in registry studio transcode play; do
%__sed -i -e 's|@LIBRARY_PATH@|%{_libdir}/%{name}:%{_libdir}|g' \
	%{buildroot}%{_bindir}/%{name}-$i.sh
done

# icons
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps

%if 0
# menu
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}-studio.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{name}-studio.sh
Icon=%{name}.png
Terminal=false
Name=FMJ-Studio
Comment=FMJ-Studio
Categories=AudioVideo;Player;
EOF
%suse_update_desktop_file %{name}-studio AudioVideo Player

%__cat > %{buildroot}%{_datadir}/applications/%{name}-registry.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{name}-registry.sh
Icon=%{name}.png
Terminal=false
Name=FMJ-Registry Editor
Comment=FMJ-Registry Editor
Categories=AudioVideo;Music;
EOF
%suse_update_desktop_file %{name}-registry AudioVideo Music
%endif

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt LICENSE README
%{_bindir}/%{name}-*.sh
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_javadir}/%{name}/*.properties
%dir %{_javadir}/%{name}/lib
%{_javadir}/%{name}/lib/*.jar
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%exclude %{_datadir}/%{name}/src.examples.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*.png
#%{_datadir}/applications/%{name}-*.desktop

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files demo
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/src.examples.*/*

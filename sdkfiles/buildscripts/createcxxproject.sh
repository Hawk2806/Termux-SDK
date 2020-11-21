echo Building CXX Project
mkdir $1/$2
echo Copying Skel Files
cp ~/.sdkfiles/projectskel/cxx/* $1/$2
cd $1/$2
echo done!

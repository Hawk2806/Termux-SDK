echo Building C Project
mkdir $1/$2
echo Copying Skel Files
cp ~/.sdkfiles/projectskel/c/* $1/$2
cd $1/$2
echo done!

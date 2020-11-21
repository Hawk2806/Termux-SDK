echo Building Python Project
mkdir $1/$2
echo Copying Skel Files
cp ~/.sdkfiles/projectskel/python/* $1/$2
echo creating venv
cd $1/$2
python -m venv venv
echo Starting venv
source venv/bin/activate
echo done!



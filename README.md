iMPoster
============

For development:

Clone the repository using SSH or HTTPS. SSH keys need to be updated first.

Make sure you have npm installed. To check for installation:

    npm --version

cd to the app:

    cd harshavamsi.github.io

Default branch is master which is what is deployed onto the github page. Make changes on the new branch and merge:

    git checkout new

The local server should start on port 8000 by default but this can be changed in your package.json file. Start local server:

    sudo npm start

This will start server on http://localhost:8000/index.html

After making changes to your new branch add commit and then switch to master:

    git add .

    git commit -m "your message"

Switch back to master and merge the new branch:

    git checkout master

    git merge new

If you've modified same lines of code on both branches you'll get a merge conflict, resolve it and commit again.    

Use "https://gist.github.com/hofmannsven/6814451" for cheatsheet.


Built with <3 using vanilla Bootstrap and AngularJs.

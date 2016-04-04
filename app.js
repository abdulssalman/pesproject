//Built by Vamsi. tats ryt biches
var app = angular.module('reddit-clone', ['ngRoute', 'firebase','ui.bootstrap']);


app.constant('fbURL', 'https://blazing-torch-8765.firebaseio.com/');
app.factory('Posts', function ($firebase, fbURL) {
    return $firebase(new Firebase(fbURL)).$asArray();
});


app.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'MainController',
            templateUrl: 'main.html'
        })
        .otherwise({
            redirectTo: '/'
        })
});


app.controller('MainController', function ($scope, $firebase, Posts) {

    
    $scope.posts = Posts;

    
    $scope.savePost = function (post) {
        if ((post.name && post.description && post.url && $scope.tauthData) ) {
            
            Posts.$add({
                
                name: post.name,
                
                description: post.description,
                
                url: post.url,
                
                votes: 0,
                
                user: $scope.tauthData.twitter.username
            });

            post.name = "";
            post.description = "";
            post.url = "";
            post.user=$scope.tauthData.twitter.username
            
        }
else if((post.name && post.description && post.url && $scope.regauthData)){
    Posts.$add({
                
                name: post.name,
                
                description: post.description,
                
                url: post.url,
                
                votes: 0,
                
                user: $scope.regauthData.password.email
            });

            
            post.name = "";
            post.description = "";
            post.url = "";
            post.user=$scope.regauthData.password.email
}
         else {
            
            alert('Sorry, you need all of those inputs to be filled or you need to be logged in!')
        }
    }

    
    $scope.addVote = function (post) {
        if($scope.tauthData || $scope.regauthData)
        {
        post.votes++;
        
        Posts.$save(post);
    }
    else{
        alert('You need to be logged in before doing that!')
    }
    }
    $scope.delVote = function (post) {
        if($scope.tauthData || $scope.regauthData)
        {
        post.votes--;
        
        Posts.$save(post);
    }
    else{
        alert('You need to be logged in before doing that!')
    }
    }
    $scope.addcmtVote = function (post,comment) {
        if($scope.tauthData || $scope.regauthData)
        {
        comment.votes++;
        
        Posts.$save(post);
    }
    else{
        alert('You need to be logged in before doing that!')
    }
    }
    $scope.delcmtVote = function (post,comment) {
        if($scope.tauthData || $scope.regauthData)
        {
        comment.votes--;
        
        Posts.$save(post);
    }
    else{
        alert('You need to be logged in before doing that!')
    }
    }

    
    $scope.deletePost = function (post) {
        if(($scope.tauthData && $scope.tauthData.twitter.username==post.user)||($scope.regauthData && $scope.regauthData.password.email==post.user)){
        var postForDeletion = new Firebase('https://blazing-torch-8765.firebaseio.com/' + post.$id);
        postForDeletion.remove();
    }
    else if($scope.tauthData || $scope.regauthData){
        alert('You cant delete others posts!')
    }
    else{
        alert('You need to be logged in before doing that!')
    }
    }

    $scope.addComment = function (post, comment) {
        if ($scope.tauthData) {
            var ref = new Firebase('https://blazing-torch-8765.firebaseio.com/' + post.$id + '/comments');
            var sync = $firebase(ref);
            $scope.comments = sync.$asArray();
            $scope.comments.$add({
                user: $scope.tauthData.twitter.username,
                text: comment.text,
                votes:0
            });
        }

        else if($scope.regauthData){
            var ref = new Firebase('https://blazing-torch-8765.firebaseio.com/' + post.$id + '/comments');
            var sync = $firebase(ref);
            $scope.comments = sync.$asArray();
            $scope.comments.$add({
                user: $scope.regauthData.password.email,
                text: comment.text,
                votes:0
            });
        } 
    
    else{
        alert('You need to be logged in before doing that!')
    }
        
        comment.text = "";
    }
    
    $scope.removeComment = function(post, comment) {
    
        var remcmt = new Firebase('https://blazing-torch-8765.firebaseio.com/' + post.$id + '/comments/' + comment.$id);
        remcmt.remove(); 
}

   $scope.dontshowName=true;
   $scope.showName=false; 
    $scope.tLogin = function () {
        if($scope.tauthData){
            alert("User already logged in");
        }
        else{
        var ref = new Firebase('https://blazing-torch-8765.firebaseio.com/');
        
        ref.authWithOAuthPopup('twitter', function (error, authData) {
            
            if (error) {
                alert('Sorry, there was an error.');
            }
            
            else {
                alert('You were logged in successfully.');
            }
            $scope.close = function(result){
  dialog.close(result);
};
            $scope.tauthData = authData;
            $scope.showName=true;
            $scope.dontshowName=false;
            $scope.username= $scope.tauthData.twitter.username;
        });
    }
    }

$scope.userSignup = function (user){
var ref = new Firebase("https://blazing-torch-8765.firebaseio.com/");
ref.createUser({
    username:user.name,
  email    : user.email,
  password : user.password
}, function(error, userData) {
  if (error) {
    alert("Error creating user");
  } else {
    alert("Successfully created user account");
  }
});
}
$scope.userLogin = function(login){
    if($scope.regauthData){
        alert("User already logged in");
    }
    else{
    var ref = new Firebase("https://blazing-torch-8765.firebaseio.com/");
ref.authWithPassword({
  email    : login.email,
  password : login.password
}, function(error, authData) {
  if (error) {
    alert("Login Failed!");
  } else {
    alert("Logged in successfully");
  }
  $scope.regauthData=authData;
  $scope.showName=true;
  $scope.dontshowName=false;
  $scope.username= $scope.regauthData.password.email;
});
}

}
$scope.logOut= function(){
    var ref = new Firebase("https://blazing-torch-8765.firebaseio.com/");
ref.unauth();
location.reload();
}



});





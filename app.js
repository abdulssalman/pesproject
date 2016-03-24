//Built by Vamsi. tats ryt biches
var app = angular.module('reddit-clone', ['ngRoute', 'firebase']);


app.constant('fbURL', 'https://unknown-chat.firebaseio.com');


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
        if (post.name && post.description && post.url && $scope.authData) {
            
            Posts.$add({
                
                name: post.name,
                
                description: post.description,
                
                url: post.url,
                
                votes: 0,
                
                user: $scope.authData.twitter.username
            });

            
            post.name = "";
            post.description = "";
            post.url = "";
        } else {
            
            alert('Sorry, you need all of those inputs to be filled or you need to be logged in!')
        }
    }

    
    $scope.addVote = function (post) {
        
        post.votes++;
        
        Posts.$save(post);
    }

    
    $scope.deletePost = function (post) {
        
        var postForDeletion = new Firebase('https://unknown-chat.firebaseio.com/' + post.$id);
        
        postForDeletion.remove();
    }

    $scope.addComment = function (post, comment) {
        if ($scope.authData) {
            var ref = new Firebase('https://unknown-chat.firebaseio.com/' + post.$id + '/comments');
            var sync = $firebase(ref);
            $scope.comments = sync.$asArray();
            $scope.comments.$add({
                user: $scope.authData.twitter.username,
                text: comment.text
            });
        } else {
            alert('You need to be logged in before doing that!')
        }
        
        comment.text = "";
    }
    
    $scope.removeComment = function(post, comment) {
        var commentForDeletion = new Firebase('https://unknown-chat.firebaseio.com/' + post.$id + '/comments/' + comment.$id);
        commentForDeletion.remove();
    }

    
    $scope.login = function () {
        
        var ref = new Firebase('https://unknown-chat.firebaseio.com/');
        
        ref.authWithOAuthPopup('twitter', function (error, authData) {
            
            if (error) {
                alert('Sorry, there was an error.');
            }
            
            else {
                alert('You were logged in successfully.');
            }
            
            $scope.authData = authData;
        });
    }
});
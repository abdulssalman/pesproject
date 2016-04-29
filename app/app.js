var app = angular.module("myApp", ["firebase"]);

app.factory("userData", ["$firebaseArray", function($firebaseArray) {
    var ref = new Firebase("https://teamproject.firebaseio.com/");
    return $firebaseArray(ref);

}]);
app.controller('TheController', ["$scope", "userData","$firebaseArray",function($scope, userData,$firebaseArray) {

$scope.userdata=userData;
 $scope.showloginerror=false;
 $scope.showregistererror=false;
 $scope.showpassworderror=false;
 $scope.showdetailserror=false;
    $scope.registeruser = function(register) {
        if (register.email && register.password && register.confirmpassword) {
            if (register.password == register.confirmpassword) {
                var ref = new Firebase("https://teamproject.firebaseio.com/");
                ref.createUser({
                  email    : register.email,
                  password : register.password
                }, function(error, userData) {
                  if (error) {
                      $scope.$apply(function(){
                          $scope.showregistererror=true;
                      });

                  } else {
                    window.location.href="/app/components/mainpage.html";
                  }
                });
                }
             else {


                         $scope.showpassworderror=true;



                register.password = "";
                register.confirmpassword = "";
            }
        } else {

                $scope.showdetailserror=true;


        }
    };

    $scope.loginuser=function(login){
        var ref = new Firebase("https://teamproject.firebaseio.com/");
ref.authWithPassword({
  email    : login.email,
  password : login.password
}, function(error, authData) {
  if (error) {
      $scope.$apply(function(){
         $scope.showloginerror=true;
      });
  } else {
      window.location.href="/app/components/mainpage.html";
       

  }
$scope.currentuser=authData;
$scope.useremail=$scope.currentuser.password.email;


});
    };


    $scope.userprofile=function(profile){
        $scope.userdata.$add({
            email:profile.email,
            firstname:profile.firstname,
            lastname:profile.lastname,
            displayname:profile.displayname,
            branch:profile.branch,
            semester:profile.semester,
            newuser:false,
        });
        alert("added");
    };


    $scope.userdata.$loaded()
.then(function(){
    angular.forEach($scope.userdata, function(user) {
        if(user.email=="vamsi@gmail.com"){
            console.log($scope.useremail);
        console.log("here");
        }
    });
});



}]);

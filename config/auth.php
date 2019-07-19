<?php
session_start();
include "config.php";

$username = $_POST['username'];
$password = hash('sha3-224',$_POST['password']);

$cek = pg_query($con, "SELECT * FROM akses WHERE username = '$username' AND password = '$password'");
$ada = pg_num_rows($cek);
$data = pg_fetch_assoc($cek);

if ($ada > 0) {
	$_SESSION['username'] = $username;
	$_SESSION['role'] = $data["role"];
	if($data["role"] == "1"){
		header("location:../pilih.php");
	}else if($data["role"]=="2"){
		header("location:../pilihbiasa.php");
	}else {
		header("location:../index.php");
	}
}else {
	header("location:../index.php");
}




$pid_script = -9999
$fail_count = -1
$tolerance = 2
"I'm checking..."
while($true)
{
	#i check if the python script exists, if not i rerun it and i save the new pid to check
	if((ps -Id $pid_script -ea SilentlyContinue) -eq $Null)
	{
		#shut down all the python process
		$new_proc = Start-Process C:\Users\path to virtualenv directory\Scripts\python.exe check_notification.py -passthru 
		$pid_script = $new_proc.Id
		Write-Host "New process created with pid: $($new_proc.Id)"
		$fail_count++
		#if the python script fails more times than allowed
		if($fail_count -gt $tolerance)
		{
			$Song=New-Object System.Media.SoundPlayer
			$Song.SoundLocation="path_to_wav"
			$Song.play()
			Start-Sleep -s 10
			$Song.stop()
			Write-Host "WARNING, THE SCRIPT HAS EXCEEDED THE MAXIMUM FAILURES THRESHOLD!"
			Break
		}
	}
	#check every 10 minutes if the python script is running
	Start-Sleep -s 600

}
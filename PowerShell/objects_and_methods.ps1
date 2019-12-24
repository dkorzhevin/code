#requires -PSEdition Core

Get-Date
$today_var = Get-Date
$today_var
Get-Member -InputObject $today_var

$today_var.Day
$today_var.DayOfWeek
$today_var.DayOfYear
$today_var.Date
$today_var.Hour
$today_var.Minute
$today_var.Second
$today_var.Year

$today_var.Hour.ToString() + ":" + $today_var.Minute.ToString() + ":" + $today_var.Second.ToString()

$today_var.Hour.GetType()
Get-Member -InputObject $today_var.Hour

$today_var.IsDaylightSavingTime()

$today_var.AddYears(1)
$today_var.AddYears(-1)
$today_next_year_var = $today_var.AddYears(1)
$today_next_year_var
$today_last_year_var = $today_var.AddYears(-1)
$today_last_year_var

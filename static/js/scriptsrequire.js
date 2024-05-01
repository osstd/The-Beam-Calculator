function updateCurrentDateTime() {
  var currentDateTimeElement = document.getElementById("currentDateTime");
  var currentDate = new Date();

  var currentYear = currentDate.getFullYear();

  document.getElementById("currentYear").innerText = currentYear;

  var dateOptions = { month: "short", day: "numeric", year: "numeric" };
  var formattedDate = currentDate.toLocaleString(undefined, dateOptions);

  var timeOptions = { hour: "numeric", minute: "numeric", hour12: true };
  var formattedTime = currentDate.toLocaleString(undefined, timeOptions);

  var formattedDateTime = formattedDate + " " + formattedTime;

  currentDateTimeElement.textContent = formattedDateTime;
}

updateCurrentDateTime();

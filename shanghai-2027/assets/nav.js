/* Shared header/nav. Kept in one file so every page stays in sync. */
(function () {
  var PAGES = [
    { href: "index.html", label: "Summary" },
    { href: "itinerary.html", label: "Itinerary" },
    { href: "hotels.html", label: "Hotels" },
    { href: "restaurants.html", label: "MICHELIN" },
    { href: "activities.html", label: "Activities" },
    { href: "ranking.html", label: "Ranking" },
    { href: "questions.html", label: "Open Questions" },
    { href: "suggestions.html", label: "Suggestions" },
    { href: "flagged.html", label: "Flagged" },
    { href: "sources.html", label: "Sources" }
  ];

  var here = location.pathname.split("/").pop() || "index.html";

  var links = PAGES.map(function (p) {
    var current = p.href === here ? ' aria-current="page"' : "";
    return '<a href="' + p.href + '"' + current + ">" + p.label + "</a>";
  }).join("");

  var html =
    '<a class="skip" href="#main">Skip to content</a>' +
    '<header class="site"><div class="bar">' +
    '<a class="brand" href="index.html"><span class="dot"></span>' +
    "<span>China Trip Planner<small>SHANGHAI · 2027</small></span></a>" +
    '<nav class="tabs" aria-label="Sections">' + links + "</nav>" +
    "</div></header>";

  document.addEventListener("DOMContentLoaded", function () {
    var mount = document.getElementById("nav");
    if (mount) mount.innerHTML = html;
  });
})();

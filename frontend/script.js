const API_URL = "http://127.0.0.1:8000";

const message = document.getElementById("message");
const results = document.getElementById("results");

function showMessage(text, isError = false) {
  message.textContent = text;
  message.style.color = isError ? "#b42318" : "#187044";
}

async function readResponse(response) {
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const detail = data.detail;
    const errorText = typeof detail === "string"
      ? detail
      : "Request failed. Please check your inputs.";
    throw new Error(errorText);
  }

  return data;
}

// Report a lost item
document.getElementById("lost-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const item = {
    item_name: document.getElementById("lost-name").value.trim(),
    description: document.getElementById("lost-description").value.trim(),
    category: document.getElementById("lost-category").value.trim(),
    location: document.getElementById("lost-location").value.trim(),
    date_lost: document.getElementById("date-lost").value
  };

  try {
    const response = await fetch(`${API_URL}/lost-items`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(item)
    });

    await readResponse(response);
    showMessage("Lost item report submitted!");
    event.target.reset();
  } catch (error) {
    showMessage(error.message, true);
  }
});

// Report a found item
document.getElementById("found-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const item = {
    item_name: document.getElementById("found-name").value.trim(),
    description: document.getElementById("found-description").value.trim(),
    category: document.getElementById("found-category").value.trim(),
    location: document.getElementById("found-location").value.trim(),
    date_found: document.getElementById("date-found").value
  };

  try {
    const response = await fetch(`${API_URL}/found-items`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(item)
    });

    await readResponse(response);
    showMessage("Found item report submitted!");
    event.target.reset();
  } catch (error) {
    showMessage(error.message, true);
  }
});

// Search lost and found items
document.getElementById("search-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const params = new URLSearchParams({
    item_type: document.getElementById("item-type").value
  });

  const keyword = document.getElementById("keyword").value.trim();
  const category = document.getElementById("search-category").value.trim();
  const location = document.getElementById("search-location").value.trim();

  if (keyword) params.set("keyword", keyword);
  if (category) params.set("category", category);
  if (location) params.set("location", location);

  results.replaceChildren();
  results.textContent = "Searching...";

  try {
    const response = await fetch(`${API_URL}/search?${params.toString()}`);
    const items = await readResponse(response);

    results.replaceChildren();

    if (!Array.isArray(items) || items.length === 0) {
      results.textContent = "No matching items found.";
      return;
    }

    items.forEach((item) => {
      const card = document.createElement("article");
      card.className = "result-card";

      const heading = document.createElement("h3");
      heading.textContent = item.item_name || "Unnamed item";

      const tag = document.createElement("span");
      tag.className = "tag";
      tag.textContent = item.item_type === "lost" ? "Lost item" : "Found item";

      const description = document.createElement("p");
      description.textContent = item.description || "No description provided.";

      const details = document.createElement("p");
      details.textContent =
        `Category: ${item.category || "—"} · Location: ${item.location || "—"}`;

      const date = document.createElement("p");
      date.textContent = `Date: ${item.date || "—"}`;

      card.append(heading, tag, description, details, date);
      results.appendChild(card);
    });
  } catch (error) {
    results.textContent = "";
    showMessage(error.message, true);
  }
});
// Select the popup and close button
const popup = document.querySelector('#messagePopup');
const closePopupBtn = document.querySelector('#closePopup');

// Select all "Send Message" buttons
const buttons = document.querySelectorAll('.send-message-btn');

// Add click event to each button
buttons.forEach((button) => {
  button.addEventListener('click', () => {
    // Get user-specific data from the button
    const userName = button.getAttribute('data-user-name');

    // Update the popup content
    document.querySelector('#popupTitle').textContent = `Send a Message to ${userName}`;

    // Show the popup
    popup.classList.remove('hidden');
  });
});

// Close the popup when the close button is clicked
closePopupBtn.addEventListener('click', () => {
  popup.classList.add('hidden');
});

// Optional: Close the popup when clicking outside of it
popup.addEventListener('click', (event) => {
  if (event.target === popup) {
    popup.classList.add('hidden');
  }
});

// Select the notification element
const connectNotification = document.querySelector('#connectNotification');

// Select all "Connect" buttons
const connectButtons = document.querySelectorAll('.connect-btn');

// Add event listener to each "Connect" button
connectButtons.forEach((button) => {
  button.addEventListener('click', () => {
    // Get user-specific data from the button's attributes
    const userName = button.getAttribute('data-user-name');
    const userId = button.getAttribute('data-user-id');

    // Log the connection request (optional)
    console.log(`Request sent to connect with ${userName} (User ID: ${userId})`);

    // Set the notification text with the user's name
    const notificationText = document.querySelector('#notificationText');
    notificationText.textContent = `request sent successfully to ${userName}`;

    // Show the notification
    connectNotification.classList.remove('hidden');

    // Automatically hide the notification after 3 seconds
    setTimeout(() => {
      connectNotification.classList.add('hidden');
    }, 3000); // Hide after 3 seconds
  });
});

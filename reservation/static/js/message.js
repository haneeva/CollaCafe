document.addEventListener("DOMContentLoaded", function() {
    // Get the message box element
    var messageBox = document.getElementById('message-box');
    
    // Check if the message box exists
    if (messageBox) {
        // Set a timeout to remove the message after 5 seconds
        setTimeout(function() {
            // Optionally, add a fade-out effect
            messageBox.style.transition = "opacity 1s ease-out";
            messageBox.style.opacity = 0;
            
            // Wait for the transition to complete, then remove the element
            setTimeout(function() {
                messageBox.style.display = 'none';
            }, 1000); // Match the duration of the fade-out effect
            
        }, 5000); // 5000 milliseconds = 5 seconds
    }
});
// to fix later on

document.addEventListener('DOMContentLoaded', function() {
    // Add to Cart button alert
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            alert('Item added to cart!');
        });
    });

    // Remove from Cart button alert
    var removeButtons = document.querySelectorAll('.remove-from-cart-btn');
    removeButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault()
            alert('Item removed from cart!');
        });
    });

    // Login button alert
    var loginButton = document.querySelector('.login-btn');
    if (loginButton) {
        loginButton.addEventListener('click', function(event) {
            alert('Login button clicked!');
        });
    }

    // Signup button alert
    var signupButton = document.querySelector('.signup-btn');
    if (signupButton) {
        signupButton.addEventListener('click', function(event) {
            alert('Sign Up button clicked!');
        });
    }
});

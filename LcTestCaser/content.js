chrome.runtime.onMessage.addListener(
    function (request, sender, sendResponse) {
        if (request.message === "clicked_browser_action") {
            // Get the test case texts
            // For problem in contest, there is a hidden `.source-content`. Ignore it.
            document.querySelector('.source-content') && document.querySelector('.source-content').remove();
            text = Array.from(document.querySelectorAll('strong, b'))
            .filter(x => x.innerText.trim() === "Input:")
            .map(x => x.nextSibling.textContent.split('\n')[0].trim())
            .map(x => x.replace(/(\,\ )?\w+\ =\ /g, '\n').trim())
            .join('\n');

            // Paste the texts into clipboard
            var copyFrom = document.createElement("textarea");

            // Set the text content to be the text you wished to copy.
            copyFrom.textContent = text;

            //Append the textbox field into the body as a child. 
            //"execCommand()" only works when there exists selected text, and the text is inside 
            //document.body (meaning the text is part of a valid rendered HTML element).
            document.body.appendChild(copyFrom);

            //Select all the text!
            copyFrom.select();

            //Execute command
            document.execCommand('copy');

            //(Optional) De-select the text using blur(). 
            copyFrom.blur();

            //Remove the textbox field from the document.body, so no other JavaScript nor 
            //other elements can get access to this.
            document.body.removeChild(copyFrom);
        }
    }
);
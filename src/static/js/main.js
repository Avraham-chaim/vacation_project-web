let sessionData;

if (window.location.pathname.includes('/vacations')) {
    document.addEventListener('DOMContentLoaded', () => {
        fetchSessionData()
            .then(() => {
                if (sessionData.current_user.role_id === 1) likeUsersLikedVacations();
            })
            .catch(error => {
                console.error('Error loading session data:', error);
            });
    });
}

// Fetch the session data from the server side:
async function fetchSessionData() {
    try{
        const response = await fetch('/get-session-data'); 
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        sessionData = await response.json();
    } catch (error) {
        console.error('Error fetching session data:', error);
    }
}

function likeUsersLikedVacations() {
    document.querySelectorAll('.like-button').forEach(likeElement => {
        const vacationId = parseInt(likeElement.dataset.vacationId);
        if (sessionData.current_user.liked_vacations.includes(vacationId)) {
            likeElement.classList.add('liked');
            likeElement.querySelector('img').src = '/static/images/icons/love.png';
        }
    });
}

function confirmDelete(url) {
    const ok = confirm("Are you sure you want to delete this vacation?");
    if (!ok) {
        event.preventDefault(); // Prevents the default action of the button
    } else {
        window.location.href = url; // Redirects if user confirms
    }
}

const errorSpan = document.querySelector(".error");
if (errorSpan) {
    setTimeout(() => {
        errorSpan.parentNode.removeChild(errorSpan);
    }, 4000);
}    

function changeLike(likeButton) {
    const likesSpan = likeButton.querySelector("span");
    const currentLikes = parseInt(likesSpan.textContent);

    let data = {
        "vacation_id":parseInt(likeButton.dataset.vacationId),
        "user_id":sessionData.current_user.user_id
    }

    if (!likeButton.classList.contains("liked")) {
        likeButton.classList.add("liked");
        likesSpan.textContent=currentLikes + 1;
        likeButton.querySelector('img').src = '/static/images/icons/love.png';
        data.liked = true;
    }
    else{
        likeButton.classList.remove("liked");
        likesSpan.textContent=currentLikes - 1;
        likeButton.querySelector('img').src = '/static/images/icons/heart.png';
        data.liked = false;
    }

    sendLikeData(data);
}

// send the like data to the server side to add/delete it to/from the DB:
async function sendLikeData(data) {
    try{
        const response = await fetch('/update-likes', {
            method:'POST', 
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return await response.json();
    } catch (error) {
        console.error('Error while passing the data:', error);
        throw error;
    }   
}

import React from 'react';

const BookmarkComponent = ({ bookmarks, onBookmarkClick }) => {
    return (
        <div className='bookmark-container'>
            <h3>Bookmarks</h3>
            <ul>
                {bookmarks.map((bookmark, index) => (
                    <li key={index} onClick={() => onBookmarkClick(bookmark)}>
                        {bookmark.name}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default BookmarkComponent;
const getCommentElement = (feedId, commentId, comment) => {
  var commentElement = document.createElement('div');
  commentElement.className = `${feedId}-${commentId}`;
  commentElement.innerHTML = `<p>${comment}</p><button onClick="onDeleteComment(${feedId}, ${commentId})">댓글 삭제</button>`;
  return commentElement;
}

const onAddComment = async (feedId) => {
  const commentInput = document.getElementsByClassName(`${feedId}-comment-input`)[0];
  let data = new FormData();
  data.append("content", commentInput.value);
  const response = await axios.post(`/feeds/${feedId}/comments/`, data);
  
  const commentId = response.data.commentId;
  const commentElement = getCommentElement(feedId, commentId, commentInput.value);
  document.getElementsByClassName(`${feedId}-comment-list`)[0].appendChild(commentElement);
  commentInput.value = '';
};

const onDeleteComment = async (feedId, commentId) => {
  await axios.delete(`/feeds/${feedId}/comments/${commentId}/`);
  const commentElement = document.getElementsByClassName(`${feedId}-${commentId}`)[0];
  commentElement.remove();
}
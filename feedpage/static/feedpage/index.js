const onLikeFeed = async (feedId) => {
  const feedLikeButton = document.getElementsByClassName(`${feedId}-like-button`)[0];
  const userLikeCount = document.getElementsByClassName('user-like-count')[0];
  const response = await axios.get(`/feeds/${feedId}/like/`);
  feedLikeButton.innerHTML = `${response.data.feedLikeCount} Likes`;
  userLikeCount.innerHTML = `내가 좋아한 글 : ${response.data.userLikeCount}개`;
}

const onDeleteFeed = async (feedId) => {
  const confirmDeleteFeed = confirm('정말 삭제하시겠습니까?');
   
  if(confirmDeleteFeed) {
    await axios.delete(`/feeds/${feedId}/delete/`);
    const feedElement = document.getElementsByClassName(`feed-${feedId}`)[0];
    feedElement.remove();
  }
}

const getTagElement = (tagContent, tagId) => {
  var newTagElement = document.createElement('a');
  newTagElement.setAttribute('href', `/tags/${tagId}/`);
  newTagElement.innerHTML = tagContent;
  return newTagElement; 
}

const onAddTag = async () => {
  const tagInputElement = document.getElementsByClassName("tag-input")[0];
  if(tagInputElement.value) {
    let data = new FormData();
    data.append("content", tagInputElement.value);
    const response = await axios.post(`/tags/new/`, data);
    const tagElement = getTagElement(tagInputElement.value, response.data.tagId);
    document.getElementsByClassName("tag-list")[0].appendChild(tagElement);
    tagInputElement.value = '';
  }
}

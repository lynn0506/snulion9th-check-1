const onClickLikeButton = async (feedId) => {
  const feedLikeButton = document.getElementsByClassName(`${feedId}-like-button`)[0];
  const userLikeCount = document.getElementsByClassName('user-like-count')[0];
  const response = await axios.get(`/feeds/${feedId}/like/`);
  feedLikeButton.innerHTML = `${response.data.feedLikeCount} Likes`;
  userLikeCount.innerHTML = `내가 좋아한 글 : ${response.data.userLikeCount}개`;
}

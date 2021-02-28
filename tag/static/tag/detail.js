const onEditTag = async (tagId) => {
  const tagInput = document.getElementsByClassName('tag-input')[0];
  if(tagInput.value) {
    let data = new FormData();
    data.append("content", tagInput.value);
    await axios.post(`/tags/${tagId}/update/`, data);
    const tagElement = document.getElementsByClassName('tag-value')[0];
    tagElement.innerHTML = tagInput.value;
  }
}
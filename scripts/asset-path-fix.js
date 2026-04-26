'use strict';

function getPosition(str, m, i) {
  return str.split(m, i).join(m).length;
}

hexo.extend.filter.register('before_post_render', function(data) {
  var config = hexo.config;
  if (!config.post_asset_folder) return;

  // 提取 slug
  var link = data.permalink;
  var beginPos = getPosition(link, '/', 3) + 1;
  var endPos = link.lastIndexOf('/') + 1;
  link = link.substring(beginPos, endPos);
  var slug = link.split('/').filter(function(elem) { return elem !== ''; }).pop();

  // 替换 Markdown 中的 ./slug/xxx 为 xxx
  // 例如: ./hello-world/2022020901.jpeg -> 2022020901.jpeg
  var pattern = new RegExp('!\\[([^\\]]*)\\]\\(\\./' + slug + '/([^)]+)\\)', 'g');

  data.content = data.content.replace(pattern, '![$1]($2)');

  return data;
});

Prism.languages.solidity = {
  'comment': [
  {
    pattern: /(^|[^\\])\/\*[\w\W]*?\*\//,
    lookbehind: true
  },
  {
    pattern: /(^|[^\\:])\/\/.*/,
    lookbehind: true
  }
  ],
  'string': /(["'])(\\(?:\r\n|[\s\S])|(?!\1)[^\\\r\n])*\1/,
  'class-name': {
    pattern: /(contract\s+)(\b[a-z0-9_]+\b)/i,
    lookbehind: true
  },
  'keyword': [
    /\b(break|case|const|continue|default|delete|do|else|for|if|in|mapping|new)\b/,
    /\b(private|public|return|returns|struct|switch|this|var|while|constant)\b/,
    /\b(modifier|suicide|contract|event|function)\b/
  ],
  'type': [
    /\b(mapping|real|string|text|msg|block|tx|ureal|address|bool|bytes)\b/,
    /\b(int|int8|int16|int24|int32|int40|int48|int56|int64|int72|int80|int88|int96)\b/,
    /\b(int104|int112|int120|int128|int136|int144|int152|int160|int168|int178|int184)\b/,
    /\b(int192|int200|int208|int216|int224|int232|int240|int248|int256)\b/,
    /\b(uint|uint8|uint16|uint24|uint32|uint40|uint48|uint56|uint64|uint72|uint80)\b/,
    /\b(uint88|uint96|uint104|uint112|uint120|uint128|uint136|uint144|uint152|uint160)\b/,
    /\b(uint168|uint178|uint184|uint192|uint200|uint208|uint216|uint224|uint232)\b/,
    /\b(uint240|uint248|uint256)\b/,
    /\b(hash|hash8|hash16|hash24|hash32|hash40|hash48|hash56|hash64|hash72|hash80)\b/,
    /\b(hash88|hash96|hash104|hash112|hash120|hash128|hash136|hash144|hash152|hash160)\b/,
    /\b(hash168|hash178|hash184|hash192|hash200|hash208|hash216|hash224|hash232)\b/,
    /\b(hash240|hash248|hash256)\b/,
    /\b(string1|string2|string3|string4|string5|string6|string7|string8|string9)\b/,
    /\b(string10|string11|string12|string13|string14|string15|string16|string17)\b/,
    /\b(string18|string19|string20|string21|string22|string23|string24|string25)\b/,
    /\b(string26|string27|string28|string29|string30|string31|string32)\b/,
    /\b(bytes1|bytes2|bytes3|bytes4|bytes5|bytes6|bytes7|bytes8|bytes9|bytes10)\b/,
    /\b(bytes11|bytes12|bytes13|bytes14|bytes15|bytes16|bytes17|bytes18|bytes19)\b/,
    /\b(bytes20|bytes21|bytes22|bytes23|bytes24|bytes25|bytes26|bytes27|bytes28)\b/,
    /\b(bytes29|bytes30|bytes31|bytes32)\b/
  ],
  'constant': /\b(true|false|wei|szabo|finney|ether)\b/,
  'boolean': /\b(true|false)\b/,
  'function': /[a-z0-9_]+(?=\()/i,
  'number': /\b-?(?:0x[\da-f]+|\d*\.?\d+(?:e[+-]?\d+)?)\b/i,
  'operator': /--?|\+\+?|!=?=?|<=?|>=?|==?=?|&&?|\|\|?|\?|\*|\/|~|\^|%/,
  'punctuation': /[{}[\];(),.:]/
}

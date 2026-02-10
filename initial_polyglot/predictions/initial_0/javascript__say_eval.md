+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' say.spec.js
+ npm run test

> test
> jest ./*

FAIL ./say.spec.js
  say
    ✓ zero (65 ms)
    ✓ one (17 ms)
    ✓ fourteen (16 ms)
    ✓ twenty (5 ms)
    ✓ twenty-two (18 ms)
    ✓ one hundred (6 ms)
    ✓ one hundred twenty-three (6 ms)
    ✓ one thousand (5 ms)
    ✓ one thousand two hundred thirty-four (7 ms)
    ✓ one million (5 ms)
    ✓ one million two (4 ms)
    ✓ one million two thousand three hundred forty-five (7 ms)
    ✓ one billion (5 ms)
    ✓ a really big number (28 ms)
    ✕ raises an error below zero (240 ms)
    ✕ raises an error above 999,999,999,999 (16 ms)

  ● say › raises an error below zero

    expect(received).toThrow(expected)

    Expected message: "Number must be between 0 and 999,999,999,999."
    Received message: "Number is out of range"

          64 |   // Check if within allowed range: 0 <= n <= 999,999,999,999
          65 |   if (n < 0 || n > 999999999999) {
        > 66 |     throw new Error('Number is out of range');
             |           ^
          67 |   }
          68 |
          69 |   // Special case for zero

      at say (say.js:66:11)
      at say.spec.js:68:10
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (say.spec.js:69:8)
      at Object.toThrow (say.spec.js:69:8)

  ● say › raises an error above 999,999,999,999

    expect(received).toThrow(expected)

    Expected message: "Number must be between 0 and 999,999,999,999."
    Received message: "Number is out of range"

          64 |   // Check if within allowed range: 0 <= n <= 999,999,999,999
          65 |   if (n < 0 || n > 999999999999) {
        > 66 |     throw new Error('Number is out of range');
             |           ^
          67 |   }
          68 |
          69 |   // Special case for zero

      at say (say.js:66:11)
      at say.spec.js:74:10
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (say.spec.js:75:8)
      at Object.toThrow (say.spec.js:75:8)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 14 passed, 16 total
Snapshots:   0 total
Time:        4.157 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/say.js|.\/say.spec.js/i.
  console.error
    Error speaking text: Command failed: espeak "nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one billion"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one million two thousand three hundred forty-five"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one million two"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one million"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one thousand two hundred thirty-four"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one thousand"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one hundred twenty-three"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one hundred"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "twenty-two"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "twenty"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "fourteen"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "one"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

  console.error
    Error speaking text: Command failed: espeak "zero"
    /bin/sh: 1: espeak: not found

      131 |     }
      132 |   });
    > 133 | };
          |   ^
      134 |

      at say.js:133:15

npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice

+ ./gradlew test
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes

> Task :compileTestJava FAILED
/testbed/src/test/java/ZipperTest.java:18: error: left has private access in Zipper
        zipper.left.setRight(new Zipper(3));
              ^
/testbed/src/test/java/ZipperTest.java:18: error: cannot find symbol
        zipper.left.setRight(new Zipper(3));
                   ^
  symbol:   method setRight(Zipper)
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:32: error: left has private access in Zipper
        assertThat(zipper.left.right.getValue()).isEqualTo(3);
                         ^
/testbed/src/test/java/ZipperTest.java:32: error: cannot find symbol
        assertThat(zipper.left.right.getValue()).isEqualTo(3);
                              ^
  symbol:   variable right
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:39: error: left has private access in Zipper
        assertThat(zipper.left.left).isNull();
                         ^
/testbed/src/test/java/ZipperTest.java:39: error: cannot find symbol
        assertThat(zipper.left.left).isNull();
                              ^
  symbol:   variable left
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:46: error: left has private access in Zipper
        assertThat(zipper.left.right.toTree()).isEqualTo(binaryTree);
                         ^
/testbed/src/test/java/ZipperTest.java:46: error: cannot find symbol
        assertThat(zipper.left.right.toTree()).isEqualTo(binaryTree);
                              ^
  symbol:   variable right
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:53: error: cannot find symbol
        assertThat(zipper.up).isNull();
                         ^
  symbol:   variable up
  location: variable zipper of type Zipper
/testbed/src/test/java/ZipperTest.java:60: error: left has private access in Zipper
        assertThat(zipper.left.up.right.up.left.right.getValue()).isEqualTo(3);
                         ^
/testbed/src/test/java/ZipperTest.java:60: error: cannot find symbol
        assertThat(zipper.left.up.right.up.left.right.getValue()).isEqualTo(3);
                              ^
  symbol:   variable up
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:67: error: left has private access in Zipper
        assertThat(zipper.left.right.up.up.getValue()).isEqualTo(1);
                         ^
/testbed/src/test/java/ZipperTest.java:67: error: cannot find symbol
        assertThat(zipper.left.right.up.up.getValue()).isEqualTo(1);
                              ^
  symbol:   variable right
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:74: error: left has private access in Zipper
        zipper = zipper.left;
                       ^
/testbed/src/test/java/ZipperTest.java:96: error: left has private access in Zipper
        zipper = zipper.left.right.up;
                       ^
/testbed/src/test/java/ZipperTest.java:96: error: cannot find symbol
        zipper = zipper.left.right.up;
                            ^
  symbol:   variable right
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:118: error: left has private access in Zipper
        zipper = zipper.left;
                       ^
/testbed/src/test/java/ZipperTest.java:143: error: left has private access in Zipper
        zipper = zipper.left;
                       ^
/testbed/src/test/java/ZipperTest.java:186: error: left has private access in Zipper
        zipper = zipper.left.right;
                       ^
/testbed/src/test/java/ZipperTest.java:186: error: cannot find symbol
        zipper = zipper.left.right;
                            ^
  symbol:   variable right
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:207: error: left has private access in Zipper
        Zipper zipper1 = binaryTree.getRoot().left.up.right;
                                             ^
/testbed/src/test/java/ZipperTest.java:207: error: cannot find symbol
        Zipper zipper1 = binaryTree.getRoot().left.up.right;
                                                  ^
  symbol:   variable up
  location: variable left of type BinaryTree
/testbed/src/test/java/ZipperTest.java:208: error: right has private access in Zipper
        Zipper zipper2 = binaryTree.getRoot().right;
                                             ^
23 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileTestJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 1s
2 actionable tasks: 2 executed

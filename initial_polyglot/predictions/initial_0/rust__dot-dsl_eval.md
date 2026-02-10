+ cargo test -- --include-ignored
   Compiling dot-dsl v0.1.0 (/testbed)
error[E0433]: failed to resolve: could not find `graph_items` in `graph`
 --> tests/dot-dsl.rs:3:21
  |
3 | use dot_dsl::graph::graph_items::edge::Edge;
  |                     ^^^^^^^^^^^ could not find `graph_items` in `graph`

error[E0433]: failed to resolve: could not find `graph_items` in `graph`
 --> tests/dot-dsl.rs:4:21
  |
4 | use dot_dsl::graph::graph_items::node::Node;
  |                     ^^^^^^^^^^^ could not find `graph_items` in `graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
 --> tests/dot-dsl.rs:9:24
  |
9 |     let graph = Graph::new();
  |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
  --> tests/dot-dsl.rs:23:24
   |
23 |     let graph = Graph::new().with_nodes(&nodes);
   |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
  --> tests/dot-dsl.rs:37:24
   |
37 |     let graph = Graph::new().with_nodes(&nodes);
   |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
  --> tests/dot-dsl.rs:54:24
   |
54 |     let graph = Graph::new().with_edges(&edges);
   |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
  --> tests/dot-dsl.rs:68:24
   |
68 |     let graph = Graph::new().with_edges(&edges);
   |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
  --> tests/dot-dsl.rs:83:24
   |
83 |     let graph = Graph::new().with_attrs(&[("foo", "1")]);
   |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
   --> tests/dot-dsl.rs:116:24
    |
116 |     let graph = Graph::new()
    |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
   --> tests/dot-dsl.rs:157:24
    |
157 |     let graph = Graph::new()
    |                        ^^^ function or associated item not found in `Graph`

error[E0599]: no function or associated item named `new` found for struct `Graph` in the current scope
   --> tests/dot-dsl.rs:182:24
    |
182 |     let graph = Graph::new().with_nodes(
    |                        ^^^ function or associated item not found in `Graph`

Some errors have detailed explanations: E0433, E0599.
For more information about an error, try `rustc --explain E0433`.
error: could not compile `dot-dsl` (test "dot-dsl") due to 11 previous errors
warning: build failed, waiting for other jobs to finish...

# docker-volume-example

🐳🔁 Example of how two docker can communicate and share files


One part of the file `deserializer` can increment the number of time the string will be on the file.
On the other hand, `serializer` can read this file and return to the user connected to the server.

They both are on disinct docker but they share the same file thanks to the docker volume.

NB: I know I inverted `serializer` and `deserializer`, I may fix it later.


NB2: The function `get_hit_count` is useless

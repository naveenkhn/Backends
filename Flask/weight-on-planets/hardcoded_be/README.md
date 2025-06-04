When you run docker build, Docker follows these steps:
	1.	Pull Base Image (if not available locally)
	•	Docker checks if the base image (python:3.11) exists locally.
	•	If not, it pulls the image from Docker Hub (or any configured registry).
	2.	Create a New Layer for Each Instruction
	•	Each command in the Dockerfile (FROM, COPY, RUN, etc.) creates a new layer.
	•	These layers are stored in Docker’s Union File System (AUFS, OverlayFS, etc.), making images lightweight and reusable.
	3.	Cache Optimization
	•	If a layer hasn’t changed, Docker reuses the cached version instead of rebuilding it.
	4.	Build Final Image
	•	After processing all layers, Docker packages everything into a single image.

When You Run a Container (docker run)
	1.	Docker Daemon Creates an Isolated Environment
	•	It assigns a unique container ID, namespace, and filesystem.
	•	The container gets a virtual network interface (usually via bridge mode).
	2.	Runs the Application in a Controlled Environment
	•	The process inside the container thinks it’s running on a fresh OS.
	•	It has only the files and dependencies copied into the image.
	3.	Resource Allocation (CPU & Memory)
	•	Docker uses cgroups (Control Groups) and namespaces to allocate resources.
    •	By default, it uses as much CPU & memory as needed, but you can limit it:
        docker run --memory=256m --cpus=0.5 weight-on-planets

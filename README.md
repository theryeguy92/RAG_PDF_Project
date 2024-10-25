<h1> Retrieval-Augmented Generation (RAG) Pipeline for PDF Querying</h1>

This project serves to illustrate, and provide an example of the functionalities of a RAG pipeline that is designed to do the following:

**1. Process and Store PDF files**

**2. Retrieve relevant document information**

**3. Generate an accurate response to the user queries.** 

This RAG project uses the following tools:

**1. __Kafka__: Message handling**

**2. __MongoDB__ for Storage**

**3. __LLaMA__: for the LLM processing via Docker**

**4. __Kubernetes__ for orchestration across the four virtual machines (VMs)**

<h1>Pipeline/Workflow Overview</h1>

### 1. PDF Upload and Processing:
- Users will be able to upload a PDF via a web interface
- PDF are preprocessed and stored in MongoDB with metadata for queries
- Kafka handles the messaging to confirm a sucessful upload

### 2. Query and Response Generation:
- Users submit questions via an interface
- The users question (query API) will retrieve the relevant content from MongoDB, send it through Kafka, and routes it to the language moel for processing.
- The language model generates a response, which will then be returned to the user.


<h1>1. Individual VM Setup</h1>

### VM1: PDF Processing and API Gateway
- **Purpose**: Handles PDF upload, text extraction, and storage.
- **Setup**:
    #### 1. Leverage Docker to create a REST API for uploading and managing PDFs.
    #### 2. Store PDFs in MongoDB(**VM4**) via a unique ID.
    #### 3. Preprocess PDFs (e.g., Convert to text, split document into sections) and store processed data in MongoDB.


### VM2: Kafka For Messaging
- **Purpose**: Manages inter-service communication for document uploads and queries
- **Setup**:
    #### 1. Stage a Kafka broker in Docker.
    #### 2. Define Kafka topics (e.g., `pdf_upload`, `queries`, `responses`) for message handling.

### VM3: AI Model and Query Handler
- **Purpose**: Hosts and processes queries through a language model.
- **Setup**:
    #### 1. Deploy LLaMA in a Docker container.
    #### 2. Stage query service to retrieve document sections from MongoDB, sends queries, and receives responses from the model.
    #### 3. Use Kubernetes to manage the service for auto-scaling with high traffic.

### VM4: MongoDB for Document Storage
- **Purpose**: Store preprocessed PDF contents and metadata.
- **Setup**:
    #### 1. Deploy MongoDB in Docker with a schema optimized for fast retrieval.
    #### 2. Enable indexing and structure data to support efficient querying.

<h2>2. Kubernetes Orchestration</h2>

- Deploy each service (API, Kafka, etc.) across Kubernetes clusters.
- Configure Kubernetes for auto-scaling, especially for the AI model.

<h2>3. Security and Performance</h2>

- Implement authentication for secure user access, and inter-service communication.
- Set up caching and indexing within MongoDB to optimize retrieval speed (minimize latency).

<h2>4. Testing and Monitoring</h2>

- Measure end-to-end testing for each service, and entire pipeline to ensure smooth data flow.
- Monitor VM and service performance via Prometheus for real-time performance metrics. 

<h1>Project Flow Diagram</h1>

<h2>1. PDF Upload:</h2>
    - User uploads PDF → PDF processed and stored in MongoDB → Kafka sends confirmation message.

<h2>2. Query Processing:</h2>
    - User submits a question → API retrieves relevant content from MongoDB → Content routed through Kafka to the language model.

<h2>3. Response Generation:</h2>
    - Language model generates a response → Kafka returns response to query API → API returns response to user.





    


**Kindly note that this README may change due to the requiremenets of the project**










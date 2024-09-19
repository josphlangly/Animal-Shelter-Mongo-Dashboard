# Animal Shelter Dashboard

### Overview
This **Animal Shelter Dashboard** is a web-based application built using `Dash` that integrates with a MongoDB database to manage animal records. The dashboard enables users to filter, visualize, and interact with animal data through CRUD operations and various rescue type filters. It also includes geolocation mapping for selected animals.

---

## Features

- **CRUD Operations**: The application allows users to perform CRUD (Create, Read, Update, Delete) operations on animal shelter data stored in MongoDB.
- **Interactive Data Table**: Users can filter the animal data by different rescue types (Water Rescue, Mountain Rescue, Disaster Rescue) and view the results in a sortable, pageable table.
- **Data Visualization**: 
  - Pie charts displaying animal breed distribution.
  - Geolocation mapping that pinpoints the location of selected animals.
- **Dynamic Dashboard**: The dashboard is built using `Dash` and offers real-time interaction with MongoDB data.

---

## Installation and Setup

### Requirements:
- **Python 3.x**
- **MongoDB**: Either a local instance or a remote MongoDB service like MongoDB Atlas.
- **Dash**: A Python framework for building analytical web applications.
- **Dash Leaflet**: For adding map and geolocation features.

### Python Libraries:
- `dash`
- `dash-leaflet`
- `jupyter-dash`
- `pandas`
- `numpy`
- `plotly`
- `pymongo`

You can install the necessary libraries using the following command:
```bash
pip install dash jupyter-dash dash-leaflet pandas numpy plotly pymongo
```

### Steps to Run the Project:

1. **MongoDB Setup**:
   - Ensure your MongoDB instance is running locally or remotely.
   - Update the `AnimalShelter` class with your MongoDB credentials (`username`, `password`, `host`, and `port`).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/animal-shelter-dashboard.git
   cd animal-shelter-dashboard
   ```

3. **Run the App**:
   You can start the Dash app by running the Python file. If you are using Jupyter Notebooks, you can run it directly in the notebook.
   ```bash
   python app.py
   ```

4. **Access the Dashboard**:
   Once the app is running, you can access the dashboard in your browser at `http://127.0.0.1:8050`.

---

## Usage

### Filter by Rescue Types:

The dashboard provides filtering options based on rescue types:
- **Water Rescue**: Filters breeds suitable for water rescues.
- **Mountain Rescue**: Filters breeds suitable for mountain rescues.
- **Disaster Rescue**: Filters breeds suitable for disaster rescues.
- **Reset**: Displays all records without any filter.

### Data Table:

- The data table displays animal records from the MongoDB database. You can:
  - **Sort** by column values.
  - **Page** through the data.
  - **Select** an individual row to highlight an animal.

### Visualizations:

- **Pie Chart**: Displays a pie chart showing the distribution of breeds based on the filtered data.
- **Geolocation Map**: Shows the location of the selected animal on a map with markers. The map centers around Austin, Texas.

---

## Code Components

### 1. `AnimalShelter` Class:

- Connects to the MongoDB instance and provides CRUD methods for interacting with animal data.
  - **Create**: Inserts a new record into the MongoDB collection.
  - **Read**: Queries records from the MongoDB collection.
  - **Update**: Updates existing records in the MongoDB collection.
  - **Delete**: Removes records from the MongoDB collection.

### 2. **Dash Application**:

- **Interactive Table**: Displays MongoDB data, allows filtering by rescue types, and supports sorting and pagination.
- **Pie Chart**: Visualizes the distribution of animal breeds in a pie chart format.
- **Map**: Uses Dash Leaflet to plot the location of selected animals on a map.

### 3. **Callbacks**:

- The application uses Dash callbacks to handle interaction between the components:
  - **Filter**: Filters data based on the selected rescue type.
  - **Graph Update**: Updates the pie chart based on the filtered data.
  - **Map Update**: Updates the geolocation map based on the selected animal.

---

## Future Enhancements

- **Advanced Filtering**: Add more advanced filtering options, such as by age, gender, or adoption status.
- **Detailed Animal Profiles**: Allow users to view more detailed profiles of individual animals, including medical history and adoption records.
- **User Authentication**: Implement a user authentication system for authorized data manipulation.
- **Mobile Support**: Enhance the dashboard for better mobile and tablet usability.

---

## Technologies Used

- **Python**: The primary language for this project.
- **MongoDB**: Used for storing animal shelter data.
- **Dash**: Framework for building the interactive dashboard.
- **Dash Leaflet**: Library for integrating maps and geolocation features.
- **pandas**: Used for data manipulation.
- **plotly**: Used for creating interactive visualizations.

---

## Contact

- **Author**: Joseph Langley
- **Email**: [joseph.o.langley@gmail.com](mailto:joseph.o.langley@gmail.com)

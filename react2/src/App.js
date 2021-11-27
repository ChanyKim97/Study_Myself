import React, { useState } from "react";
import Movie from "./components/Movie";
import MovieForm from "./components/MovieForm";

function App() {
  const [movies, setMovies] = useState(
    //[{title : 'Movie1',year : 2001},{title : 'Movie2',year : 2002},{title : 'Movie3',year : 2003}]
    []
  );

  const removeMovie = (id) =>{
    setMovies(movies.filter(movie=>{
      return movie.id !== id;
    }))
  };

  const renderMovies = movies.length ? movies.map(movie => {
    return (
      <Movie 
        movie={movie} 
        key={movie.id}
        removeMovie={removeMovie}
      />
    );
  }) : '추가된 영화 없슴';

  const addMovie = (movie) =>{
    setMovies([
      ...movies,
      movie
    ]);
  };

  return (
    <div className="App">
      <h1>Movie List</h1>
      <MovieForm addMovie={addMovie}/>
      {renderMovies}
    </div>
  );
}

export default App;

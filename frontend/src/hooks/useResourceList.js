import { useState, useEffect } from "react";
import axios from "axios";

const useResourceList = url => {
  const [resourceList, setResourceList] = useState([]);

  const fetchResourceList = url =>
    axios.get(url).then(response => {
      setResourceList(response.data);
    });

  useEffect(() => {
    fetchResourceList(url);
  }, [url]);

  return resourceList;
};

export default useResourceList;

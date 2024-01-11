<template>
  <div class="contents">
    <!--<h1>{{ msg }}</h1> -->

    <div class="search-box">
      <label for="search">Search:</label>
      <input type="text" id="search" placeholder="Type to search..." />
    </div>

    <div>
      <table id="myTable">
        <thead>
          <tr>
            <th>Date</th>
            <th>Title</th>
            <th>Type</th>
            <th>Platform</th>
            <th>Author</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <tr
            v-for="(item, index) in rows"
            :key="index"
            :class="{ 'odd-tr': (index + 1) % 2 === 1, 'even-tr': (index + 1) % 2 === 0 }"
          >
            <td>{{ item.cell1 }}</td>
            <td>
              <router-link to="/details">{{ item.cell2 }}</router-link>
            </td>
            <td>{{ item.cell3 }}</td>
            <td>{{ item.cell4 }}</td>
            <td>{{ item.cell5 }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- 页数切换器 -->
    <ul class="pagination">
      <li><a href="#">Previous</a></li>
      <li class="current"><a href="#">1</a></li>
      <li><a href="#">2</a></li>
      <li><a href="#">3</a></li>
      <li><a href="#">4</a></li>
      <li><a href="#">5</a></li>
      <li>...</li>
      <li><a href="#">100</a></li>
      <li><a href="#">Next</a></li>
    </ul>
    <div class="bottom-blank"></div>
  </div>
</template>

<script>

export default {
  name: "Main",
  data() {
    return {
      msg: "Welcome to CodeSecLab",
      rows: Array.from({ length: 16 }, (_, index) => ({
        cell1: `2024-1-10`,
        cell2: `OpenPLC WebServer 3 - Denial of Service`,
        cell3: `DoS`,
        cell4: `Multiple`,
        cell5: `Kai Feng`,
      })),
    };
  },

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bottom-blank{
  height: 60px;
}
.odd-tr {
  background-color: #f2f2f2;
}
.even-tr {
  background-color: #ffffff; 
}

/* 页数切换器容器样式 */
.pagination {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 20px;
  float: right;
}

/* 切换按钮共用样式 */
.pagination li {
  margin-right: 5px;
}

/* 当前页样式 */
.pagination li.current {
  font-weight: bold;
}

#search {
  height: 30px;
  font-size: 16px;
}

.search-box {
  top: 0;
  right: 0;
  margin-top: 10px;
  margin-right: 10px;
  float: right;
  padding: 20px 0;
}
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

th {
  background-color: #f2f2f2;
}
.contents {
  margin-top: 0px;
  margin: 0;
  text-align: center;
}
</style>

<script>
  import { PUBLIC_API_URL } from "$env/static/public";
  import "iconify-icon";
</script>

<body class="bg-[#fbf3eb]">
  <div class="h-screen flex items-center justify-center">
    <form
      action="{PUBLIC_API_URL}/api/get-img"
      enctype="multipart/form-data"
      method="post"
    >
      <div class="grid grid-cols-1 place-items-center">
        <div class="mb-11">
          <label
            for="fileInput"
            class="upload h-[300px] w-[300px] text-center p-[30%] text-8xl"
            ><iconify-icon icon="lucide:upload" style="color: #6a6355"
            ></iconify-icon></label
          >
          <input id="fileInput" type="file" name="file" />
        </div>
        <div><input type="submit" value="Convert" /></div>
      </div>
    </form>
  </div>
</body>

<style>
  input[type="submit"] {
    border-style: solid;
    border-width: 2px;
    border-radius: 13px;
    color: #fbf3eb;
    padding: 1em 0.75em;
    background-color: #0c3d26;
    cursor: pointer;
    font-weight: normal;
    width: 300px;
  }
  input[type="file"] {
    display: none;
  }

  .upload {
    border-style: dashed;
    border-width: 2px;
    border-color: #6a6355;
    border-radius: 13px;
    color: black;
    background-color: #fdfaf6;
    cursor: pointer;
    text-transform: uppercase;
    font-weight: normal;
    box-shadow: 0px 0px 0px black;
    display: inline-block;
    opacity: 90%;
  }
</style>

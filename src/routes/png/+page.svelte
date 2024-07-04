<script>
  import { PUBLIC_API_URL } from "$env/static/public";
  import "iconify-icon";
</script>

<svelte:head>
  <title>Imgtools - Convert to PNG</title>
</svelte:head>

<body>
  <div class="h-screen flex items-center justify-center">
    <form
      action="{PUBLIC_API_URL}/api/get-png"
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
        <div><input type="submit" value="Convert to PNG" /></div>
      </div>
    </form>
  </div>
</body>

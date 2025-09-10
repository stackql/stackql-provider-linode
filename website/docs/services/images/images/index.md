--- 
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - images
  - linode
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage linode resources using SQL
custom_edit_url: null
image: /img/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.images.images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_image"
    values={[
        { label: 'get_image', value: 'get_image' },
        { label: 'get_images', value: 'get_images' }
    ]}
>
<TabItem value="get_image">

A single image object.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The unique identifier for each image. (example: linode/debian11)</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ A list of the possible capabilities of this image.  - `cloud-init`. The image supports the cloud-init multi-distribution method with our [Metadata service](https://www.linode.com/docs/products/compute/compute-instances/guides/metadata/#troubleshoot-metadata-and-cloud-init). This only applies to public images.  - `distributed-sites`. Whether the image can be used in distributed compute regions. Compared to a core compute region, distributed compute regions offer limited functionality, but they're globally distributed. Your image can be geographically closer to you, potentially letting you deploy it quicker. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for complete details.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this image was created. (example: 2021-08-14T22:44:02)</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The name of the user who created this image, or `linode` for public images. (example: linode)</td>
</tr>
<tr>
    <td><CopyableCode code="deprecated" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__, __Read-only__ Whether this image is deprecated. Only public images can be deprecated.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A detailed description of this image. (example: Example image description.)</td>
</tr>
<tr>
    <td><CopyableCode code="eol" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date of the public image's planned removal from service. This is `null` for private images. (example: 2026-07-01T04:00:00)</td>
</tr>
<tr>
    <td><CopyableCode code="expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ Only images created automatically from a deleted compute instance (type=automatic) expire. This is `null` for private images.</td>
</tr>
<tr>
    <td><CopyableCode code="is_public" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__, __Read-only__ Revealed as `true` if the image is a public distribution image. Private, account-specific images are listed as `false`.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ A short description of the image. (example: Debian 11)</td>
</tr>
<tr>
    <td><CopyableCode code="regions" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ Details on the regions where this image is stored. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for full details on support for `regions`. (x-linode-cli-format: json)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The minimum size in MB this image needs to deploy.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The current status of the image. Possible values are `available`, `creating`, and `pending_upload`.  &gt; 📘 &gt; &gt; The `+order_by` and `+order` operators are not available when [filtering](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) on this key. (example: available)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>__Filterable__ Tags used for organizational purposes. A tag can be from 3 to 100 characters long, and an image can have a maximum of 500 total tags.</td>
</tr>
<tr>
    <td><CopyableCode code="total_size" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total size in bytes of all instances of this image, in all `regions`.  &gt; 📘 &gt; &gt; This object is empty for existing images. It's intended for use with future functionality.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ How the image was created. Create a `manual` image at any time. An `automatic` image is created automatically from a deleted compute instance. (example: manual)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this image was last updated. (example: 2021-08-14T22:44:02)</td>
</tr>
<tr>
    <td><CopyableCode code="vendor" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The upstream distribution vendor. This is `null` for private images. (example: Debian)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_images">

A paginated list of images.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The current [page](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="pages" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="results" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total number of results.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get_image"><CopyableCode code="get_image" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get information about a single image. An image can be one of two types:<br /><br />- **Public image**. The `id` for these images begins with `linode/`. These images are generally available to all users. To limit the response to public images, don't include [authentication](https://techdocs.akamai.com/linode-api/reference/get-started#authentication) when calling this operation.<br /><br />- **Private image**. The `id` for these images begins with `private/`. These images are account-specific and only accessible to users with appropriate [grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants). To view private images, you need to include authentication when calling this operation. The response will also include public images.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_images"><CopyableCode code="get_images" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of images. An image can be one of two types:<br /><br />- **Public image**. The `id` for these images begins with `linode/`. These images are generally available to all users. To limit the response to public images, don't include [authentication](https://techdocs.akamai.com/linode-api/reference/get-started#authentication) when calling this operation.<br /><br />- **Private image**. The `id` for these images begins with `private/`. These images are account-specific and only accessible to users with appropriate [grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants). To view private images, you need to include authentication when calling this operation. The response includes both private and public images.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_image"><CopyableCode code="post_image" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__disk_id"><code>data__disk_id</code></a></td>
    <td></td>
    <td>Captures a private, gold-master image from a Linode disk.<br /><br />&gt; 📘<br />&gt;<br />&gt; - When you capture an image, we store it using our Object Storage service. The `region` where the target image exists determines where the [resulting image is stored](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-captured-custom-images).<br />&gt;<br />&gt; - When you create a new image, we automatically encrypt it for its protection. Images remain encrypted at rest, in storage, in caching, and in transit. When you deploy an image to a [new](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-a-new-compute-instance) or [existing](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-an-existing-compute-instance) Linode, we automatically decrypt it. If you've enabled encryption for a Linode you want to create an image of, we also encrypt the image. When you deploy that image, the image is decrypted and the resulting disk will be automatically encrypted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_image"><CopyableCode code="put_image" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a private image that you have permission to `read_write`.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can't update the `regions` with this operation. Use the [Replicate an image](https://techdocs.akamai.com/linode-api/reference/post-replicate-image) operation to modify the existing regions for your image.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_image"><CopyableCode code="delete_image" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a private image you have permission to `read_write`.<br /><br />&gt; 🚧<br />&gt;<br />&gt; - You can't undo this delete action.<br />&gt;<br />&gt; - When you delete an image, all [replicated instances](https://techdocs.akamai.com/linode-api/reference/post-replicate-image) of that image are also deleted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_upload_image"><CopyableCode code="post_upload_image" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-label"><code>label</code></a>, <a href="#parameter-region"><code>region</code></a></td>
    <td></td>
    <td>Creates a new private image container and returns a URL as the `upload_to` object in the response. Use this URL to upload your own disk image to the container.<br /><br />1. Ensure the disk image is raw disk image (`.img`) format.<br /><br />2. Compress the disk image using gzip (`.gz`) format. Compressed, the file can be up to 5 GB and decompressed it can be up to 6 GB.<br /><br />3. Upload the file in a separate PUT request that includes the `Content-type: application/octet-stream` header:<br /><br />  ```<br />  curl -v \<br />    -H "Content-Type: application/octet-stream" \<br />    --upload-file example.img.gz \<br />    $UPLOAD_URL \<br />    --progress-bar \<br />    --output /dev/null<br />  ```<br /><br />&gt; 📘<br />&gt;<br />&gt; - You need to upload image data within 24 hours of creation or the API cancels the upload and deletes the image container.<br />&gt;<br />&gt; - Only core regions that support our [Object Storage](https://techdocs.akamai.com/cloud-computing/reference/how-to-choose-a-data-center#product-availability) service can store an uploaded image.<br />&gt;<br />&gt; - When you create a new image, we automatically encrypt it for its protection. Images remain encrypted at rest, in storage, in caching, and in transit. When you deploy an image to a [new](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-a-new-compute-instance) or [existing](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-an-existing-compute-instance) Linode, we automatically decrypt it. If you've enabled encryption for a Linode you want to create an image of, we also encrypt the image. When you deploy that image, the image is decrypted and the resulting disk will be automatically encrypted.<br />&gt;<br />&gt; - You can create a new image and upload image data using a single process through [Cloud Manager](https://www.linode.com/docs/products/tools/images/guides/upload-an-image/#uploading-an-image-file-through-the-cloud-manager) or the [Linode CLI](https://www.linode.com/docs/products/tools/images/guides/upload-an-image/#uploading-an-image-file-through-the-linode-cli).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_replicate_image"><CopyableCode code="post_replicate_image" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Target an existing image and replicate it to another compute region.<br /><br />&gt; 📘<br />&gt;<br />&gt; As part of our limited promotional period, image replicas are free of charge until November 1, 2025. After this date, replicas will be subject to our standard monthly rate of $0.10/GB. When replicas become billable, your monthly charge will be calculated using the value returned in `total_size`, divided by 100. [Learn more](https://www.linode.com/blog/compute/image-service-improvements-akamai-cdn/).<br /><br />- This is only available in a `region` that supports Object Storage, which stores the replicated image. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to review a region's `capabilities`.<br /><br />- To replicate an image, it needs to have a `status` of `available`. Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation to view an image's `status`.<br /><br />- To also keep the target image in its original compute region, you need to include that `region` in the request's data. If you leave it out, the API removes the image from that region. Run the [Get an image](https://techdocs.akamai.com/linode-api/reference/get-image) operation to see the `regions` where an image currently exists.<br /><br />- You can't include an empty array to delete all images. You need to provide at least one compute `region` where the image is `available`. Use the [Delete an image](https://techdocs.akamai.com/linode-api/reference/delete-image) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>The page of a collection to return.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The number of items to return per page.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_image"
    values={[
        { label: 'get_image', value: 'get_image' },
        { label: 'get_images', value: 'get_images' }
    ]}
>
<TabItem value="get_image">

Get information about a single image. An image can be one of two types:<br /><br />- **Public image**. The `id` for these images begins with `linode/`. These images are generally available to all users. To limit the response to public images, don't include [authentication](https://techdocs.akamai.com/linode-api/reference/get-started#authentication) when calling this operation.<br /><br />- **Private image**. The `id` for these images begins with `private/`. These images are account-specific and only accessible to users with appropriate [grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants). To view private images, you need to include authentication when calling this operation. The response will also include public images.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
capabilities,
created,
created_by,
deprecated,
description,
eol,
expiry,
is_public,
label,
regions,
size,
status,
tags,
total_size,
type,
updated,
vendor
FROM linode.images.images;
```
</TabItem>
<TabItem value="get_images">

Returns a paginated list of images. An image can be one of two types:<br /><br />- **Public image**. The `id` for these images begins with `linode/`. These images are generally available to all users. To limit the response to public images, don't include [authentication](https://techdocs.akamai.com/linode-api/reference/get-started#authentication) when calling this operation.<br /><br />- **Private image**. The `id` for these images begins with `private/`. These images are account-specific and only accessible to users with appropriate [grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants). To view private images, you need to include authentication when calling this operation. The response includes both private and public images.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.images.images
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_image"
    values={[
        { label: 'post_image', value: 'post_image' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_image">

Captures a private, gold-master image from a Linode disk.<br /><br />&gt; 📘<br />&gt;<br />&gt; - When you capture an image, we store it using our Object Storage service. The `region` where the target image exists determines where the [resulting image is stored](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-captured-custom-images).<br />&gt;<br />&gt; - When you create a new image, we automatically encrypt it for its protection. Images remain encrypted at rest, in storage, in caching, and in transit. When you deploy an image to a [new](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-a-new-compute-instance) or [existing](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-an-existing-compute-instance) Linode, we automatically decrypt it. If you've enabled encryption for a Linode you want to create an image of, we also encrypt the image. When you deploy that image, the image is decrypted and the resulting disk will be automatically encrypted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.images.images (
data__cloud_init,
data__description,
data__disk_id,
data__label,
data__tags
)
SELECT 
{{ cloud_init }},
'{{ description }}',
{{ disk_id }} --required,
'{{ label }}',
'{{ tags }}'
RETURNING
id,
capabilities,
created,
created_by,
deprecated,
description,
eol,
expiry,
is_public,
label,
regions,
size,
status,
tags,
total_size,
type,
updated,
vendor
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: images
  props:
    - name: cloud_init
      value: boolean
      description: >
        Whether this image supports [cloud-init](https://www.linode.com/docs/guides/write-files-with-cloud-init/).
        
    - name: description
      value: string
      description: >
        A detailed description of this image.
        
    - name: disk_id
      value: integer
      description: >
        The ID of the target Linode disk for this image.
        
    - name: label
      value: string
      description: >
        The short title for this image. If not provided, the disk's current label is used.
        
    - name: tags
      value: array
      description: >
        Tags used for organizational purposes. A tag can be from 3 to 100 characters long, and an image can have a maximum of 500 total tags.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_image"
    values={[
        { label: 'put_image', value: 'put_image' }
    ]}
>
<TabItem value="put_image">

Updates a private image that you have permission to `read_write`.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can't update the `regions` with this operation. Use the [Replicate an image](https://techdocs.akamai.com/linode-api/reference/post-replicate-image) operation to modify the existing regions for your image.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.images.images
SET 
data__description = '{{ description }}',
data__label = '{{ label }}',
data__tags = '{{ tags }}'
WHERE 

RETURNING
id,
capabilities,
created,
created_by,
deprecated,
description,
eol,
expiry,
is_public,
label,
regions,
size,
status,
tags,
total_size,
type,
updated,
vendor;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_image"
    values={[
        { label: 'delete_image', value: 'delete_image' }
    ]}
>
<TabItem value="delete_image">

Deletes a private image you have permission to `read_write`.<br /><br />&gt; 🚧<br />&gt;<br />&gt; - You can't undo this delete action.<br />&gt;<br />&gt; - When you delete an image, all [replicated instances](https://techdocs.akamai.com/linode-api/reference/post-replicate-image) of that image are also deleted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.images.images;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_upload_image"
    values={[
        { label: 'post_upload_image', value: 'post_upload_image' },
        { label: 'post_replicate_image', value: 'post_replicate_image' }
    ]}
>
<TabItem value="post_upload_image">

Creates a new private image container and returns a URL as the `upload_to` object in the response. Use this URL to upload your own disk image to the container.<br /><br />1. Ensure the disk image is raw disk image (`.img`) format.<br /><br />2. Compress the disk image using gzip (`.gz`) format. Compressed, the file can be up to 5 GB and decompressed it can be up to 6 GB.<br /><br />3. Upload the file in a separate PUT request that includes the `Content-type: application/octet-stream` header:<br /><br />  ```<br />  curl -v \<br />    -H "Content-Type: application/octet-stream" \<br />    --upload-file example.img.gz \<br />    $UPLOAD_URL \<br />    --progress-bar \<br />    --output /dev/null<br />  ```<br /><br />&gt; 📘<br />&gt;<br />&gt; - You need to upload image data within 24 hours of creation or the API cancels the upload and deletes the image container.<br />&gt;<br />&gt; - Only core regions that support our [Object Storage](https://techdocs.akamai.com/cloud-computing/reference/how-to-choose-a-data-center#product-availability) service can store an uploaded image.<br />&gt;<br />&gt; - When you create a new image, we automatically encrypt it for its protection. Images remain encrypted at rest, in storage, in caching, and in transit. When you deploy an image to a [new](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-a-new-compute-instance) or [existing](https://techdocs.akamai.com/cloud-computing/docs/deploy-an-image-to-an-existing-compute-instance) Linode, we automatically decrypt it. If you've enabled encryption for a Linode you want to create an image of, we also encrypt the image. When you deploy that image, the image is decrypted and the resulting disk will be automatically encrypted.<br />&gt;<br />&gt; - You can create a new image and upload image data using a single process through [Cloud Manager](https://www.linode.com/docs/products/tools/images/guides/upload-an-image/#uploading-an-image-file-through-the-cloud-manager) or the [Linode CLI](https://www.linode.com/docs/products/tools/images/guides/upload-an-image/#uploading-an-image-file-through-the-linode-cli).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.images.images.post_upload_image 
@@json=
'{
"cloud_init": {{ cloud_init }}, 
"description": "{{ description }}", 
"label": "{{ label }}", 
"region": "{{ region }}", 
"tags": "{{ tags }}"
}';
```
</TabItem>
<TabItem value="post_replicate_image">

Target an existing image and replicate it to another compute region.<br /><br />&gt; 📘<br />&gt;<br />&gt; As part of our limited promotional period, image replicas are free of charge until November 1, 2025. After this date, replicas will be subject to our standard monthly rate of $0.10/GB. When replicas become billable, your monthly charge will be calculated using the value returned in `total_size`, divided by 100. [Learn more](https://www.linode.com/blog/compute/image-service-improvements-akamai-cdn/).<br /><br />- This is only available in a `region` that supports Object Storage, which stores the replicated image. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to review a region's `capabilities`.<br /><br />- To replicate an image, it needs to have a `status` of `available`. Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation to view an image's `status`.<br /><br />- To also keep the target image in its original compute region, you need to include that `region` in the request's data. If you leave it out, the API removes the image from that region. Run the [Get an image](https://techdocs.akamai.com/linode-api/reference/get-image) operation to see the `regions` where an image currently exists.<br /><br />- You can't include an empty array to delete all images. You need to provide at least one compute `region` where the image is `available`. Use the [Delete an image](https://techdocs.akamai.com/linode-api/reference/delete-image) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.images.images.post_replicate_image 
@@json=
'{
"regions": "{{ regions }}"
}';
```
</TabItem>
</Tabs>
